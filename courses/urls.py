from django.urls import path

from .views import CoursesAPIView, RatingsAPIView, CourseAPIView, RatingAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('ratings/<int:pk>/', RatingAPIView.as_view(), name='rating'),
]
