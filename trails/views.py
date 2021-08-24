from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import HikeSerializer
from .models import Hike
from .permissions import IsAuthorOrReadOnly

class HikeList(ListCreateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer

class HikeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
