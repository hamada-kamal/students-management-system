from django.db import models
from django.db.models.deletion import PROTECT
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Level(models.Model):
    name = models.CharField(max_length=40) 
    slug = models.SlugField(blank = True , null = True)

    def __str__(self):
        return self.name
    
    def save(self , *args  ,**kwargs ):
        self.slug = slugify(self.name)
        super(Level , self).save( *args , **kwargs)



    def get_absolute_url(self):
        return reverse('course:get_subjects', args=[str(self.id)])



class Subject(models.Model):
    semester_category = [
        ('semester1','semester1'),
        ('semester2','semester2'),
    ]
    name = models.CharField(max_length=100)
    level = models.ForeignKey(Level,on_delete=models.PROTECT)
    semester = models.CharField(max_length=50, choices=semester_category) 
    code = models.CharField(max_length=8, unique=True)
    slug = models.SlugField(blank = True , null = True)

    def __str__(self):
        return self.name

    def save(self , *args  ,**kwargs ):
        self.slug = slugify(self.name)
        super(Subject , self).save( *args , **kwargs)

    def get_absolute_url(self):
        return reverse('course:get_lectures', args=[str(self.id)])





class Lecture(models.Model):
    lec_category = [
        ('lecture','lecture'),
        ('section','section'),
        ('lab','lab'),
    ]
    adminupload = models.FileField(upload_to='lecture_files', verbose_name='Lecture File')
    title = models.CharField(max_length=38) 
    belongs_to = models.ForeignKey(Subject, on_delete=models.PROTECT)
    type = models.CharField(max_length=40, choices=lec_category, verbose_name='Lecture Type')

    def __str__(self):
        return self.title


