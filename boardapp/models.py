from django.db import models

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_user = models.CharField(max_length=50)
    imgs = models.ImageField(upload_to='') #settings.pyで設定したところに保存される
    good = models.IntegerField()
    read = models.IntegerField()
    readtext = models.TextField()