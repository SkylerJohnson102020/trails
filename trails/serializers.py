from rest_framework.serializers import ModelSerializer
from .models import Hike

class HikeSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'trail_name', 'description')
        model = Hike
