from rest_framework import viewsets
from .serializer import ProgrammerSerializer, StudentSerializer
from .models import programmer
from .models import Student

# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer