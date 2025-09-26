# Example script to create roles
from django.contrib.auth.models import Group, Permission

def create_roles():
    # Admin role
    admin_group, _ = Group.objects.get_or_create(name='admin')
    # Editor role
    editor_group, _ = Group.objects.get_or_create(name='editor')
    # Viewer role
    viewer_group, _ = Group.objects.get_or_create(name='viewer')
