from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Card
from .serializers import CardSerializer


class CardList(ListAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()


class CardDetail(RetrieveAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
