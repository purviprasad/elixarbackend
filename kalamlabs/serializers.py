
from rest_framework import serializers
from . import models

class KalamRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KalamRegistration
        fields = '__all__'

class BookFreeTrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BookAFreeTrial
        fields = '__all__'