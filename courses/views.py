from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializers


class CourseAPIView(APIView):
    """
    Course API
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RatingAPIView(APIView):
    """
    Rating API
    """
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializers(ratings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
