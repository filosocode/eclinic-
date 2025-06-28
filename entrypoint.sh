#!/bin/sh

echo "Esperando a que la base de datos esté disponible..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

echo "Base de datos disponible, aplicando migraciones..."
python manage.py migrate

# Crear superusuario si no existe
echo "Verificando superusuario..."
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('AIATIC', 'admin@aiatic.com', 'AIATIC')
" | python manage.py shell

echo "Iniciando el servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
