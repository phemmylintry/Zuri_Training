from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


# Create your views here.

#making a post request
class StudentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)


# @api_view(['POST'])
# def create_student(request):
#     # student = Student.objects.all()
#     serializer = StudentSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


class GetStudentViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UpdateStudentViews(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DeleteStudentViews(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer  