# Bosscha Plate Archive

This project is to help digitalization Bosscha's Plate Archive

## Development

* Clone this project
* Create virtual environment, we assume `virtualenvironmentwrapper` already installed

```bash
$ mkvirtualenv bosscha_plate_archive # do it once
$ workon bosscha_plate_archive
```

* Install Requirements

```bash
$ pip install -r bosscha_plate_archive/requirements.txt
```

* Change directory to `bosscha_plate_archive/bosscha_plate_archive` and copy `.env.example` then paste as `.env`. Add all credentials in `.env`

```bash
$ cd bosscha_plate_archive/bosscha_plate_archive
$ cp .env.example .env 
```

* Move to above directory, migrate and run

```bash
$ cd ..
$ python manage.py migrate
$ python manage.py runserver 
```

* Open http://localhost:8000

* Costumize admin interface color

```bash
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```