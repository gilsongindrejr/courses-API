from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializers


class CourseAPIView(APIView):
    """
    API for courses
    """
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class RatingAPIView(APIView):
    """
    API for rating
    """
    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializers(ratings, many=True)
        return Response(serializer.data)
