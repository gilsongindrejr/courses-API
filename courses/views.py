from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializers
from .permissions import AuthenticatedReadOnly, AuthenticatedPostOnly

"""
API V1
"""


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


"""
API V2
"""


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (AuthenticatedReadOnly,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def ratings(self, request, pk=None):
        self.pagination_class.page_size = 5
        ratings = Rating.objects.all()
        page = self.paginate_queryset(ratings)

        if page is not None:
            serializer = RatingSerializers(page, many=True)
            return self.get_paginated_response(serializer.data)

        course = self.get_object()
        serializer = RatingSerializers(course.rating.all(), many=True)
        return Response(serializer.data)


class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = (AuthenticatedPostOnly,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
