from django.db import models
from django.urls import reverse
# Create your models here.

class Roadtrips(models.Model):
    name = models.CharField(max_length=150)
    estimated_drive = models.IntegerField() 
    estimated_budget = models.IntegerField()
    notes = models.TextField()
    location_1 = models.CharField(max_length=250)
    state = models.CharField(max_length=100)
    type_of_place = models.CharField(max_length=250)
    location_2 = models.CharField(max_length=250)
    state_2 = models.CharField(max_length=100)
    type_of_place_2 = models.CharField(max_length=250)
    location_3 = models.CharField(max_length=250)
    state_3 = models.CharField(max_length=100)
    type_of_place_3 = models.CharField(max_length=250)
    total_cost = models.IntegerField()
    total_length_of_trip = models.IntegerField()

    def __str__(self):
        return self.name
    
    def __get_absolute_url__(self):
        return f"/roadtrip/{self.id}"

class Stays(models.Model):
    lodging_name = models.CharField(max_length=250)
    state = models.CharField(max_length=100)
    type_of_place = models.CharField(max_length=250)
    cost = models.IntegerField()
    length_of_stay = models.IntegerField()
    notes = models.TextField()

    def __str__(self):
        return self.lodging_name
    
    def __get_absolute_url__(self):
        return f"/stay/{self.id}"

class User(models.Model):
    name = models.CharField(max_length=250)
    address = models.TextField()
    vehicle = models.TextField()
    requirements_for_trip = models.TextField()

    def __str__(self):
        return self.name

class Roadtripping(models.Model):
    roadtrip = models.ForeignKey(Roadtrips, on_delete=models.CASCADE, default=1, related_name="roadtripping")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="roadtripping")
    def __str__(self):
        return self.roadtrip.name

class Lodging(models.Model):
    stay = models.ForeignKey(Stays, on_delete=models.CASCADE, default=1, related_name="lodging")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name="lodging")
    def __str__(self):
        return self.stay.lodging_name

class PlanningLodging(models.Model):
    roadtrip = models.ForeignKey(Roadtrips, on_delete=models.CASCADE, default=1, related_name="planningLodging")
    stay = models.ForeignKey(Stays, on_delete=models.CASCADE, default=1, related_name="planningLodging")
    def __str__(self):
        return self.roadtrip.name

