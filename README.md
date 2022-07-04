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

# 인증

1. /swagger/ 로 접속
2. /token/ api로 access_token을 얻습니다.
3. Authorize 버튼을 누릅니다.
4. value 값으로 "Bearer {access_token}"을 넣습니다.

# (개발)swagger_auto_schema 예시

https://stackoverflow.com/questions/69492599/how-to-specify-example-value-on-drf-yasg-swagger-auto-schema-request-body
