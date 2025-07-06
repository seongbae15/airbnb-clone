from django.db import models
from common.models import CommonModel


# Create your models here.
class Room(CommonModel):
    "Room model definition"

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="South Korea")
    city = models.CharField(max_length=80, default="Seoul")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        blank=True,
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self):
        return self.amenities.count()

    def rating(self):
        count = self.reviews.count()
        if count == 0:
            return "No reviews"
        else:
            return round(
                sum(
                    [
                        review_rating["rating"]
                        for review_rating in self.reviews.all().values("rating")
                    ]
                )
                / count,
                2,
            )


class Amenity(CommonModel):
    "Amenity model definition"

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
