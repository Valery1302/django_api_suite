from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
import firebase_admin
from datetime import datetime
import os

class LandingAPI(APIView):

    name = "Landing API"
    collection_name = "responses"

    def _check_firebase(self):
        # 1) Firebase inicializado
        if not firebase_admin._apps:
            return Response(
                {"error": "Firebase no está inicializado (firebase_admin.initialize_app no corrió)."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        # 2) Database URL (necesaria para firebase_admin.db.reference)
        if not os.getenv("FIREBASE_DB_URL"):
            return Response(
                {"error": "Falta la variable FIREBASE_DB_URL en Railway (Realtime Database URL)."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        return None  # todo OK

    def get(self, request):
        fail = self._check_firebase()
        if fail:
            return fail

        try:
            ref = db.reference(self.collection_name)
            data = ref.get() or []   # si no hay nada, devuelve algo válido
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "Error accediendo a Firebase", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        fail = self._check_firebase()
        if fail:
            return fail

        try:
            data = request.data.copy()

            ref = db.reference(self.collection_name)

            current_time  = datetime.now()
            custom_format = current_time.strftime("%d/%m/%Y, %I:%M:%S %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
            data.update({"timestamp": custom_format})

            new_resource = ref.push(data)
            return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": "Error guardando en Firebase", "detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
