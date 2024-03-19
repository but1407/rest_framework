from django.urls import path,include,re_path
from .views import CourseViewSet,LessonViewSet,UserViewSet,ExampleView,UserCountView
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register('courses',CourseViewSet)
route.register('lessons',LessonViewSet)
route.register('users',UserViewSet)
# route.register('example/',ExampleView)

# route.register('users2',UserViewSet2)



urlpatterns = [
    # path('',views.Index),
    path('',include(route.urls)),
    path('example/',ExampleView.as_view(),name='example'),
    path('usercount/',UserCountView.as_view(),name='count'),
    
    

]