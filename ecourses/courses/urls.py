from django.urls import path,include,re_path
from .views import CourseViewSet,LessonViewSet,UserViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('courses',CourseViewSet)
route.register('lessons',LessonViewSet)
route.register('users',UserViewSet)



urlpatterns = [
    # path('',views.Index),
    path('',include(route.urls)),

]