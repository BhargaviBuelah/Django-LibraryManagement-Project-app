from django.db import models


# Create your models here.
class Book(models.Model):#Applicationname_classname =>libraryapp_book
    
    bname=models.CharField(max_length=50)
    bdesc=models.CharField(max_length=100)
    bauthor=models.CharField(max_length=50)
    copies=models.FloatField()
    price=models.FloatField()
    cat=models.CharField(max_length=10)
    is_deleted=models.CharField(max_length=5)
    uid=models.IntegerField()



    def __str__(self):

        return self.bname
    