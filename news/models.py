from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    contents = models.CharField(max_length=200)
    def __str__(self):
        output = 'Title: ' + self.title + '\nPublished: ' + str(self.publish_date) + '\n'
        return output