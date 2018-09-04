from django.db import models

class Post(models.Model):
    abc=models.CharField(max_length=250)
    pqr=models.CharField(max_length=250)
class Person(models.Model):
    key=models.ForeignKey(Post,on_delete=models.CASCADE)
    abc1=models.CharField(max_length=250)
    pqr2=models.CharField(max_length=250)
