from django.contrib import admin
from exam_interview.models import *

# Register your models here.

class exam_model_admin(admin.ModelAdmin):
    list_display = ["id","questions"]

admin.site.register(exam_model,exam_model_admin)

class Contact_Model_Admin(admin.ModelAdmin):
    list_display=['id','username','email','phone','desc']
    
admin.site.register(Contact_Model,Contact_Model_Admin)