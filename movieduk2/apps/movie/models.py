from django.db import models
from movieduk.custom_models import ListField
from .choices import GENRE_CHOICES

class popularity(models.Model):
  page_view

class Movie(models.Model):
  code  = models.IntegerField(primary_key=True)

  mains = models.ManyToManyField('Role', related_name='mains')
  subs = models.ManyToManyField('Role', related_name='subs')
  staffs = models.ManyToManyField('Role', related_name='staffs')
  directors = models.ManyToManyField('Person')

  genre = models.ManyToManyField('Genre')
  nation = models.ManyToManyField('Nation')
  form = models.ForeignKey('Form', null = True)
  grade_ko = models.ForeignKey('Grade_ko', null = True)
  grade_us = models.ForeignKey('Grade_us', null = True)

  title_ko = models.CharField(default = '', max_length=100, blank=True)
  title_en = models.CharField(default = '', max_length=100, blank=True, null=True)

  story_short = models.TextField(default = '', blank=True, null=True)
  story_long = models.TextField(default = '', blank=True, null=True)
  making_note= models.TextField(default = '', blank=True, null=True)

  time = models.SmallIntegerField(null=True) # runtime
  year = models.SmallIntegerField(null=True)

  open_year = models.DateTimeField(null=True)

  poster_url = models.SlugField(null=True)
  # http://movie.naver.com/movie/bi/mi/photoListJson.nhn?movieCode=89627&size=8&offset=8
  photo_url = ListField()
  official_url = models.SlugField(null=True)
  external_url = models.SlugField(null=True)

  rank = models.IntegerField(null=False, default = 0)

  def __unicode__(self):
    return u"%s" % self.title_ko

class Person(models.Model):
  awards = models.ManyToManyField('Award')

  code = models.IntegerField(primary_key=True)

  name_ko = models.CharField(max_length=50, null=True, blank=True)
  name_en = models.CharField(max_length=50, null=True, blank=True)

  thumb_url = models.SlugField(null=True)
  external_url = models.SlugField(null=True)

  bio = models.TextField(blank=True, null=True)
  birth = models.CharField(max_length=50, null=True, blank=True)

  def __unicode__(self):
    return u"%s" % self.name

class Award(models.Model):
  movie = models.ManyToManyField('Movie')

  year = models.SmallIntegerField(null=True, blank=True)
  title =  models.CharField(max_length=50, null=True, blank=True)
  award =  models.CharField(max_length=50, null=True, blank=True)
  round = models.IntegerField(null=True, blank=True)

  def __unicode__(self):
    return u"%s (%s)" %(self.title, self.award)

class Role(models.Model):
  person = models.ForeignKey('Person')

  role = models.CharField(max_length=30, null=True, blank=True)
  title = models.CharField(max_length=30, null=True, blank=True)

  def __unicode__(self):
    return u"%s : %s (%s)" %(self.role, self.person.name, self.title)

class Genre(modles.Model):
  """
    - get_genre_display() => return Genre string
    - in template => {{ OBJNAME.get_FIELDNAME_display }}
  """
  genre = models.CharField(max_length=2, choices=GENRE_CHOICES) 

  def __unicode__(self):
    return u"%s" % self.get_genre_display()

class Nation(modles.Model):
  nation = models.CharField(max_length=2, choices=NATION_CHOICES)

  def __unicode__(self):
    return u"%s" % self.get_nation_display()

class Form(models.Model):
  form = models.CharField(max_length=1, choices=FORM_CHOICES)

  def __unicode__(self):
    return u"%s" % self.get_form_display()

class Grade_ko(models.Model):
  grade_ko = models.CharField(max_length=1, choices=GRADE_KO_CHOICES)

  def __unicode__(self):
    return u"%s" % self.get_grade_ko_display()

class Grade_us(models.Model):
  grade_us = models.CharField(max_length=1, choices=GRADE_US_CHOICES)

  def __unicode__(self):
    return u"%s" % self.get_grade_us_display()
