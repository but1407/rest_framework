from django import forms
from .models import Lesson
from ckeditor_uploader import CKEditorUploadingWidget

class LessonForm(forms.Form):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'