# 번역 파일 만들기

```shell
python manage.py makemessage -l {language}
ex) python manage.py makemessage -l ko
```

위 명령어를 치면 .po파일이 만들어 진다. msgid는 원본 text이고, msgstr은 번역될 text이다.

# 번역파일 컴파일

```shell
python manage.py compilemessages
```

위 명령어를 치면 .mo파일이 만들어 진다. 이 파일이 실제 번역 역할을 하는 것 같다.