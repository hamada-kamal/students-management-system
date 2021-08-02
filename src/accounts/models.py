from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
''' 
    username
    password 
    first_name
    last_name
    email  
     '''





class Profile(models.Model):
    department_categories = [
        ('primary level','primary level'),
        ('electronics & communications','electronics & communications'),
        ('computer engineering','computer engineering'),
        ('medical engineering','medical engineering'),
        ('electrical engineering','electrical engineering'),
        ('mechanical engineering','mechanical engineering'),
    ]
    type_categories = [
        ('doctor','doctor'),
        ('stuff','stuff'),
        ('student','student'),
    ]
    level_categories = [
        ('primary level','primary level'),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        
    ]
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True , blank=True)
    addres = models.CharField(max_length=50 , blank=True, null=True)
    image = models.ImageField(upload_to = 'student_pic', blank=True, null=True)
    student_id = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=50, choices=level_categories, blank=True, null=True)
    department = models.CharField(max_length=50, choices=department_categories, blank=True, null=True)
    type = models.CharField(max_length=50, choices=type_categories, blank=True, null=True)
    # Job

    def __str__(self):
        return str(self.user)


@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Profile.objects.create(
            user = instance
        )
