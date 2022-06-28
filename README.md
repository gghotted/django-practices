# secret files

## ./.env

docker-compose를 위한 변수 파일

- POSTGRES_DB: db 이름
- POSTGRES_USER: user 이름
- POSTGRES_PASSWORD: user password
- NGINX_SERVER_NAME: servername (localhost)

## ./django_site/.secrets

### common.json

```json
// example
{
    "SECRET_KEY": "key",
    "EMAIL_HOST_USER": "email@gmail.com",
    "EMAIL_HOST_PASSWORD": "app_password"
}
```

### debug.json

```json
// example
{
    "ALLOWED_HOSTS": ["*"],
    "DEBUG": true,
    "CELERY_BROKER_URL": "localhost",
    "CELERY_RESULT_BACKEND": "localhost"
}
```

### deploy.json

```json
// example
{
    "ALLOWED_HOSTS": ["*"],
    "DATABASES": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dbname",
        "USER": "username",
        "PASSWORD": "1234",
        "HOST": "postgres"
    },
    "DEBUG": false,
    "CELERY_BROKER_URL": "redis",
    "CELERY_RESULT_BACKEND": "redis"
}
```

# 실행

## docker-compose

```shell
docker-compose --env-file .env up
```

## debug mode

```shell
docker run --name redis-django -p 6379:6379 redis
```

```shell
cd django_site
export DJANGO_SETTING_MODULE=django_site.settings.debug
celery -A django_site worker -l debug --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo
```

```shell
cd django_site
python manage.py runserver
```

