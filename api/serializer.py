from rest_framework import serializers
from .models import programmer, Student

class ProgrammerSerializer(serializers.ModelSerializer):
   class Meta:
       model = programmer
       #fields= ('fullname','nickname','age')
       fields = '__all__'
       
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'