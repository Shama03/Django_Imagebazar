from django.db import models

class Catogory(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self):
        return self.title 


class Image(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    image= models.ImageField(upload_to='images')
    added_date= models.DateTimeField()
    cat= models.ForeignKey(Catogory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title 
 