from django.urls import path

from .views import CoursesAPIView, RatingsAPIView, CourseAPIView, RatingAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>/', CourseAPIView.as_view(), name='course'),
    path('courses/<int:course_pk>/ratings/', RatingsAPIView.as_view(), name='course_ratings'),
    path('courses/<int:course_pk>/ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='course_rating'),

    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('ratings/<int:rating_pk>/', RatingAPIView.as_view(), name='rating'),
]
