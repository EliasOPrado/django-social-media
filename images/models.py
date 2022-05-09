from django.db import models
from django.conf import settings

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    image = models.ImageField(updload_to='images/%d/%m/%Y')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title