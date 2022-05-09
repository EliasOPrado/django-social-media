from django.db import models
from django.conf import settings
from django.utils import slugfy

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

    def save(self, *args, **kwargs):
        # transform title into slug-
        # using the slugfy() function.
        if not self.slug:
            self.slug = slugfy(self.title)
        super().save(*args, **kwargs)