from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins, status, filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny



from .models import(
    Lost
)


from .serializers import (
    LostListSerializer,
    LostSerializer,
    LostCreateSerializer,

)

from django_filters import rest_framework as rest_filter
from .permissions import IsOwner



class LostViewSet(ModelViewSet):
    queryset = Lost.objects.all()
    # print(queryset)
    serializer_class = LostSerializer
    filter_backends = [filters.SearchFilter,
    rest_filter.DjangoFilterBackend,
    filters.OrderingFilter]
    search_fields = ['title']
    filterset_fields = ['category']
    ordering_fields = ['created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return LostListSerializer
        elif self.action == 'create':
            return LostCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()











