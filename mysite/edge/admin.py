from django.contrib import admin
#making character model have admin interface
from .models import Character
admin.site.register(Character)
