from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import action
from .models import Course,Lesson,Tag,User
from rest_framework import viewsets,permissions,generics
from .serializers import CourseSerializer,LessonSerializer,UserSerializer,CommentSerializer
from rest_framework.response import Response
from rest_framework  import status
from rest_framework.parsers  import MultiPartParser
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics 

from rest_framework.renderers import JSONRenderer,TemplateHTMLRenderer
# Create your views here.

class ExampleView(APIView):
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        return Response({'received data': request.data})
    
class UserViewSet(viewsets.ViewSet,
                generics.CreateAPIView,
                generics.RetrieveAPIView,
                ):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser,]
    def get_permissions(self):
        # if self.action == 'retrieve':
        #     return [permissions.IsAuthenticated]
        return [permissions.AllowAny()]
    
class CourseViewSet(viewsets.ModelViewSet,):
        queryset = Course.objects.filter(active=True) 
        serializer_class = CourseSerializer
        permission_classes = [permissions.IsAuthenticated]
        swagger_schema= None
        def get_permissions(self):
            if self.action == 'list':
                return [permissions.AllowAny()]
            return [permissions.IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    queryset= Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer
    
    @action(methods=['post'] ,detail=True,url_path='hide_lesson',url_name='hide-lesson')
    def hide_lesson(self,request,pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        return Response(LessonSerializer(l,context ={'request':request}).data,status = 200)
        
def Index(requesst):
    lessons = Lesson.objects.filter(course__subject__icontains='java')
    course =Course.objects.filter(lessons__active=True)
    # gan tag
    # Tag_create = Tag.objects.create(name = "java core")
    # l =Lesson.objects.get(pk=1)
    # l.tags.add(Tag_create)
    # l.save()
    # lay ra tag
    t=Tag.objects.get(pk=4)
    
    t.lesson_set.all()
    return HttpResponse(t)


class UserViewSet2(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class UserCountView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'user': self.object}, template_name='template.html')

# class CommentView:
#      def __init__(self,comment ):
#         CommentSerializer.__init__(self,comment)
#         self.comment =comment 
        
        