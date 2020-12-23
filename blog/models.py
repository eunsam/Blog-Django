from django.db import models

class Blog(models.Model):
    b_title=models.CharField(max_length=50)
    b_detail=models.CharField(max_length=500)

    def __str__(self) :
        return self.b_title

# Create your models here.
