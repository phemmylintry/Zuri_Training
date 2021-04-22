from django.urls import path
from . import views

urlpatterns = [
   path('create-student/', views.StudentViews.as_view(), name="student"),
   path('get-student/', views.GetStudentViews.as_view(), name="get-student"),
   path('update-student/<int:pk>/', views.UpdateStudentViews.as_view(), name="update-student"),
   path('delete-student/<int:pk>/', views.DeleteStudentViews.as_view(), name="delete-student")
]
