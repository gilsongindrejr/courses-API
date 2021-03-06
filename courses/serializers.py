from django.db.models import Avg
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

    def validate_rating(self, value):
        if 1 < value < 6:
            return value
        raise serializers.ValidationError('The rating must be in between 1 and 5')


class CourseSerializer(serializers.ModelSerializer):

    ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    ratings_average = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created',
            'active',
            'ratings',
            'ratings_average'
        )

    def get_ratings_average(self, obj):
        avg = obj.ratings.aggregate(Avg('rating')).get('rating__avg')

        if avg is None:
            return 0
        return round(avg * 2) / 2
