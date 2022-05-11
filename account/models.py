from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%d/%m/%Y', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'

class Contact(models.Model):
    """
    model to create users relationship. 
    usage:
    user1 = User.objects.get(id=1)
    user2 = User.objects.get(id=2)
    Contact.objects.create(user_from=user1, user_to=user2)
    """
    # 

    user_from = models.ForeignKey('auth.User', 
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('auth.User',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'