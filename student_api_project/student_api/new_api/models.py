from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    department = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Student"

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
