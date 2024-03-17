from rest_framework.serializers import ModelSerializer
from .models import Course,Lesson,Tag,User



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id","first_name", "last_name", "email", "password", "avatar"]
        extra_kwargs = {  #bổ sung một số thông tin ràng của fields
            'password':{
                'write_only':'true' #bổ sung rằng password chỉ dùng để tạo chứ k hiển thị ra ngoài
            }
            }
    def create(self, validated_data):
        user =  User(**validated_data)
        user.set_password(validated_data['password'])    
        user.save()
        return user

class CourseSerializer(ModelSerializer):
    class Meta:
        model =Course
        fields =["id","subject",'image','created_at','updated_at']

class TagSerializer(ModelSerializer):
    class Meta:
        model= Tag
        fields = ['id','name']
        
class LessonSerializer(ModelSerializer):
    tags =TagSerializer(many=True)
    class Meta:
        model = Lesson
        fields =["id","subject","content","created_at","updated_at","tags","active","image"]
        