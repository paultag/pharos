from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from ...utils import import_google_latitude_file
from ...models import PharosPoint


class Command(BaseCommand):
    args = '<fpath> <user>'
    help = 'Loads in Google Latitude history.'

    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError('need file path and user')

        fpath, user = args
        import_google_latitude_file(fpath, user)
