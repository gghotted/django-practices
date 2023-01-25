export DJANGO_SETTINGS_MODULE=django_embed.settings.deploy && \
python manage.py makemigrations && \
python manage.py migrate && \
echo yes | python manage.py collectstatic && \

gunicorn --log-level=DEBUG --bind 0.0.0.0:8000 --timeout 1200 django_embed.wsgi.deploy:application