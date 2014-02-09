from django.db import models

class DukUser(models.Model):
  username = models.CharField(max_length=30)
  first_name = models.CharField(max_length=10, blank=True, null=True)
  last_name = models.CharField(max_length=10, blank=True, null=True)
  password = models.CharField(max_length=30)

  email = models.EmailField(blank=True, null=True)
  last_login = models.DateTimeField(blank=True, null=True)
  is_active = models.BooleanField(default=True)

  tag_movie
  rated
  reviews
  like
  watched
  watchlist

  follow

  #objects = CustomUserManager()

  def __unicode__(self):
    return self.username

  def is_authenticated(self):
    return True
