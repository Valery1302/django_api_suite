from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# Módulos requeridos por el punto 4.a
from firebase_admin import db
from datetime import datetime

from .models import Task
from .serializers import TaskSerializer

class LandingApiIndex(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response(
            {
                "name": "Landing API",
                "message": "Usa /api/token/ para obtener un token y luego consume /landing/api/tasks/",
                "endpoints": {"token": "/api/token/", "tasks": "/landing/api/tasks/"},
            },
            status=status.HTTP_200_OK,
        )
    def post(self, request):
      data = request.data
      ref = db.reference(f'{self.collection_name}')
      current_time  = datetime.now()
      custom_format = current_time.strftime("%d/%m/%Y, %I:%M:%S %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
      data.update({"timestamp": custom_format })
      new_resource = ref.push(data)
      return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)    
        

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "priority"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "due_date", "priority", "status"]
    ordering = ["-created_at"]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)