from django.db import models

class Goods(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/pics',max_length=100,null=True)
    price=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)


    def __str__(self):
        return self.name


