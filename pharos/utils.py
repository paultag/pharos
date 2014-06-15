from feedparser import _parse_date as parse_date
from lxml import etree
from time import mktime
import datetime as dt

from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User
from django.contrib.gis.geos import fromstr
from .models import PharosPoint


def import_google_latitude_file(path, user):
    coord = None
    when = None
    tree = etree.parse(open(path, 'r'))
    track = tree.xpath("//*[local-name()='Track']")[0]

    owner = User.objects.get(username=user)
    lkpt = None

    for node in track.iter():
        name = node.xpath("local-name()")
        if name == 'coord':
            lon, lat, z = node.xpath("text()")[0].split()
            coord = {
                "lat": lat,
                "lon": lon,
                "zee": z
            }
        elif name == 'when':
            when = node.xpath("text()")[0]
            pt = mktime(parse_date(when))
            if lkpt is None or pt < lkpt:
                lkpt = pt

            when = dt.datetime.fromtimestamp(pt)

        if coord and when:
            point = fromstr("POINT({lon} {lat})".format(**coord))
            PharosPoint(timestamp=when, user=owner, point=point).save()
