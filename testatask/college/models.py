from django.db import models

class Student(models.Model):
  surname = models.CharField(max_length = 30)
  name = models.CharField(max_length = 30)
  patronymic = models.CharField(max_length = 30)
  birthday = models.DateField()
  number = models.CharField(max_length = 10)
  group = models.ForeignKey('Group')

  def __unicode__(self):
      return self.get_full_name()

  @models.permalink
  def get_absolute_url(self):
      return ('update-student', [str(self.pk)])

  def get_full_name(self):
      return u'%s %s %s' % (self.surname, self.name, self.patronymic)

class Group(models.Model):
  title = models.CharField(max_length = 6)
  senior = models.ForeignKey(Student, related_name = 'senior_set', blank = True, null = True)

  def __unicode__(self):
      return self.title

  @models.permalink
  def get_absolute_url(self):
      return ('retrieve-group', [str(self.pk)])
