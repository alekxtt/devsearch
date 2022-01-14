from django.contrib import admin

from .models import Projects, Review, Tag

admin.site.register(Projects)
admin.site.register(Review)
admin.site.register(Tag)
