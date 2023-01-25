# secret files

## ./.env

docker-compose를 위한 변수 파일

- POSTGRES_DB: db 이름
- POSTGRES_USER: user 이름
- POSTGRES_PASSWORD: user password
- NGINX_SERVER_NAME: servername (localhost)

## ./django_embed/.secrets

### common.json

```json
// example
{
    "SECRET_KEY": "key"
}
```

### debug.json

```json
// example
{
    "ALLOWED_HOSTS": ["*"],
    "DEBUG": true
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
    "DEBUG": false
}
```

# 실행

```shell
docker-compose --env-file .env up
```

