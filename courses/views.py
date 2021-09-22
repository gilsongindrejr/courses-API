from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializers


class CoursesAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RatingsAPIView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))
        return self.queryset.all()


class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

    def get_object(self):
        if self.kwargs.get('course_pk'):
            return get_object_or_404(
                self.get_queryset(),
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('rating_pk')
            )
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('rating_pk'))
