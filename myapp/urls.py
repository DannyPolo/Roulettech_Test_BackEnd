from django.urls import path
from . import views


urlpatterns = [
    path("student/", views.StudentListCreate.as_view(), name="student-create-view"),
    path("student/<int:pk>/", views.StudentRetrieveUpdateDestroy.as_view(), name="student-update-view")
]
