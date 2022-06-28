export DJANGO_SETTINGS_MODULE=django_site.settings.deploy && \
python manage.py makemigrations && \
python manage.py migrate && \
echo yes | python manage.py collectstatic && \

celery -A django_site worker -l debug --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo &
gunicorn --log-level=DEBUG --bind 0.0.0.0:8000 --timeout 1200 django_site.wsgi.deploy:application