from django.contrib import admin
from .models import Project, Link
from solo.admin import SingletonModelAdmin
from homepage.models import SiteConfiguration

admin.site.register(Project)
admin.site.register(Link)
admin.site.register(SiteConfiguration, SingletonModelAdmin)
