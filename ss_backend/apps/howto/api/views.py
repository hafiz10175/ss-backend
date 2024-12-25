from rest_framework import viewsets, permissions

from .serializers import HowToSerializer
from ..models import Note

class HowToViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = HowToSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter_by_user(self.request.user).select_related("created_by", "category").prefetch_related("tags")

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
