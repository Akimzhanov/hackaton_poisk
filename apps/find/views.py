from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import AllowAny

from .models import Find
from .serializers import FindSerializer, FindListSerializer,FindCreateSerializer
from django_filters import rest_framework as rest_filter

from .permissions import IsOwner



class FindViewSet(ModelViewSet):
    queryset = Find.objects.all()
    serializer_class = FindSerializer
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
            return FindListSerializer
        elif self.action == 'create':
            return FindCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['destroy', 'update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()








