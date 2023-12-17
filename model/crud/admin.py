from django.contrib import admin
from .models import Person, Gender, News

admin.site.register(Person)
admin.site.register(Gender)
admin.site.register(News)