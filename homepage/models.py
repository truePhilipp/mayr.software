from django.db import models
from solo.models import SingletonModel


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='links')
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class SiteConfiguration(SingletonModel):
    introduction_text = models.TextField(default='Hello World!')
    language_text = models.TextField(default='')
    contact_text = models.TextField(default='')

    def __str__(self):
        return 'Site Configuration'

    class Meta:
        verbose_name = 'Site Configuration'
