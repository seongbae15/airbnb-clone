from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from rest_framework import serializers


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "id",
            "name",
            "description",
        )


class RoomListSerializer(ModelSerializer):
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "country",
            "city",
            "price",
            "rating",
        )

    def get_rating(self, room):
        return room.rating()


class RoomDetailSerializer(ModelSerializer):
    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.rating()
