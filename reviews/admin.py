from django.contrib import admin
from .models import teacher
from .models import student
from .models import course
# Register your models here.

#One to One Relation
@admin.register(teacher)
class teacherAdmin(admin.ModelAdmin):
    list_display=['teacher_name','teacher_id','user']



#Many to One Relationship
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=['student_name','student_reg','user']

#Many to Many Relationship

@admin.register(course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['course_name','course_code','Course_teacher']