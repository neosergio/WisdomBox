from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Card
from .serializers import CardSerializer


class CardList(APIView):
    """
    List all cards
    """
    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)


class CardDetail(APIView):
    def get(self, request, card_id):
        """
        Get card details
        """
        card = get_object_or_404(Card, pk=card_id)
        serializer = CardSerializer(card)
        return Response(serializer.data)
