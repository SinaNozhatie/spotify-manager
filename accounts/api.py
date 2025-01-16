from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SpotifyAccount, Member
from .serializers import SpotifyAccountSerializer, MemberSerializer

class SpotifyAccountViewSet(viewsets.ModelViewSet):
    queryset = SpotifyAccount.objects.all()
    serializer_class = SpotifyAccountSerializer

    @action(detail=True, methods=['get'])
    def slots(self, request, pk=None):
        account = self.get_object()
        return Response({
            'total_slots': 5,
            'available_slots': account.available_slots,
            'used_slots': 5 - account.available_slots
        })

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
