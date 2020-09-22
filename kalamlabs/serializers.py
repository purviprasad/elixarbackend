
from rest_framework import serializers
from . import models

class KalamRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.KalamRegistration
        fields = '__all__'