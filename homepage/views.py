from django.shortcuts import render
from .models import Project, SiteConfiguration


def homepage(request):
    return render(request, 'homepage/index.html', {
        'projects': Project.objects.order_by('-order'),
        'configuration': SiteConfiguration.get_solo()
    })
