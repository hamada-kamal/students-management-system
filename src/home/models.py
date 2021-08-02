from django.db import models
from django.contrib.auth.models import User
from course.models import Subject
from django.db.models.signals import post_save
from django.dispatch import receiver

class Complaint(models.Model):
    # class Meta:
    #     ordering = ['-created']

    Complaint_text = models.TextField(max_length=200, verbose_name='Make a complaint with unknown identity in 200 characters')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Complaint date at: " + str(self.created_at.strftime("%d %b %Y %H:%M:%S"))


class Registraion(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        Registraion.objects.create(
            user = instance
        )


