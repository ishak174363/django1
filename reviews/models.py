from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#One to One Relationship
class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    teacher_name=models.CharField(max_length=40)
    teacher_id=models.IntegerField()

#Many to One Relationship
class student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=25)
    student_reg=models.IntegerField()

#Many to May Relations
class course(models.Model):
    user=models.ManyToManyField(User)
    course_name=models.CharField(max_length=40)
    course_code=models.IntegerField()

    def Course_teacher(self):
     return "  ,  ".join([str(p) for p in self.user.all()])

