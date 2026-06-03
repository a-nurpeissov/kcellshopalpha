FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && python manage.py shell -c \"from django.contrib.auth import get_user_model; User = get_user_model(); import os; username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'morfisy'); email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'kiribaaaa@icloud.com'); password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'azimkhan1'); User.objects.filter(username=username).exists() or User.objects.create_superuser(username=username, email=email, password=password)\" && python manage.py runserver 0.0.0.0:8000"]
