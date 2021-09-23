from rest_framework import serializers

from .models import Course, Rating


class RatingSerializers(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Rating
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created',
            'active',
        )


class CourseSerializer(serializers.ModelSerializer):

    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'active',
            'ratings'
        )
