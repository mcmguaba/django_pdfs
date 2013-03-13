from django.db import models

# Create your models here.

class PDF(models.Model):
    cover_story = models.CharField(max_length=200)
    issue = models.PositiveIntegerField()
    pub_date = models.DateField('date published', db_index=True)
    thumbnail = models.ImageField(upload_to="thumbnails")
    pdf = models.FileField(upload_to="pdfs")

def __unicode__(self):
    return '%s' % self.issue
