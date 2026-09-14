import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miproyecto.settings')
django.setup()

from django.contrib.auth.models import User, Group

# Crear grupos de roles
for rol in ["admin", "normal", "viewer"]:
    Group.objects.get_or_create(name=rol)

# Crear usuario de prueba
if not User.objects.filter(username="lector").exists():
    user = User.objects.create_user("lector", password="Password123!")
    grupo_viewer = Group.objects.get(name="viewer")
    user.groups.add(grupo_viewer)
    print("Usuario 'lector' creado e integrado al grupo 'viewer'.")