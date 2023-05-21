from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)                  #제목
    contents = models.TextField()                             #내용
    create_date = models.DateTimeField(auto_now_add=True)     #날짜