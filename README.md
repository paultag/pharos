```shell
mkvirtualenv pharos --python=$(which python3)
pip install -r requirements.txt
```

```postgres
postgres=# CREATE ROLE pharos WITH LOGIN PASSWORD 'pharos';
CREATE ROLE
postgres=# CREATE DATABASE pharos OWNER pharos;
CREATE DATABASE
postgres=# \c pharos
You are now connected to database "pharos" as user "postgres".
pharos=# CREATE EXTENSION postgis;
CREATE EXTENSION
```

```shell
./manage.py syncdb
```

```
./manage.py loadgooglelatitude google-latitude-kml-file-you-exported.kml username
# You might need to go back in time to grab this.
```
