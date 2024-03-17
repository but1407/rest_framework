from django.contrib import admin
from .models import Course,Lesson,Category
from django import forms
from .models import Lesson
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.



class LessonForm(forms.ModelForm):
    content = forms.CharField(widget= CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course'

# class Course
class LessonTagInline(admin.StackedInline):
    model = Lesson.tags.through
class LessonAdmin(admin.ModelAdmin):
    class Media:
        css={
            'all':('/static/css/main.css',)
        }
    forms= LessonForm
    list_display = ["id","subject","created_at","active","updated_at","content"]
    search_fields = ["subject","created_at","course__subject"]
    list_filter =["subject","course__subject"]
    readonly_fields=["image"]
    inlines = (LessonTagInline,)
    
    # def image(self,lesson):
    #     return mark_safe("<img src='/static/{img_url}' alt='{alt}' />".format(img_url=lesson.image.name,alt=lesson.subject))
    
class CourseAdmin(admin.ModelAdmin):
    inlines=(LessonInline,)

    
admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Category)

