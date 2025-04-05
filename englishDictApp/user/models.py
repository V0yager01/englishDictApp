from django.db import models
from django.contrib.auth.models import AbstractUser

from wordsApp.models import RuToEng

user_level = (
     ('Fool', 'Fool'),
     ('Begginer', 'Begginer'),
     ('Advance', 'Advance'),
     ('Pro', 'Pro'),
     ('SuperPro', 'SuperPro')
)

class MyUser(AbstractUser):
        is_active = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_level = models.CharField(choices=user_level, default='Fool', max_length=128)

    def __str__(self) -> str:
        return 'Profile: ' + self.user.username


class Favorite(models.Model):
      word = models.ForeignKey(RuToEng, on_delete=models.CASCADE)
      user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

      class Meta:
           unique_together = ('word', 'user')
           