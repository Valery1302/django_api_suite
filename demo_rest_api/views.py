from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import uuid

data_list = []

# Datos de ejemplo
data_list.append({'id': str(uuid.uuid4()), 'name': 'eri28', 'email': 'erigutierrez@gmail.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'dani16', 'email': 'danielvillamar@gmail.com', 'is_active': True})
data_list.append({'id': str(uuid.uuid4()), 'name': 'vale09', 'email': 'valerianic09@gmail.com', 'is_active': False})


class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        active_items = [item for item in data_list if item.get('is_active', False)]
        return Response(active_items, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        if 'name' not in data or 'email' not in data:
            return Response(
                {'message': 'Faltan campos requeridos: name y email.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        new_item = {
            'id': str(uuid.uuid4()),
            'name': data.get('name'),
            'email': data.get('email'),
            'is_active': True
        }
        data_list.append(new_item)

        return Response(
            {'message': 'Dato guardado exitosamente.', 'data': new_item},
            status=status.HTTP_201_CREATED
        )


class DemoRestApiItem(APIView):
    """
    - PUT: reemplaza completamente (excepto id; id es obligatorio en body y debe coincidir con la URL)
    - PATCH: actualiza parcialmente
    - DELETE: elimina lógicamente (is_active=False)
    """

    def _find_item(self, item_id):
        for item in data_list:
            if item.get('id') == item_id:
                return item
        return None

    def put(self, request, item_id):
        data = request.data

        if 'id' not in data:
            return Response(
                {'message': 'El campo "id" es obligatorio en el cuerpo de la solicitud.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if str(data.get('id')) != str(item_id):
            return Response(
                {'message': 'El "id" del cuerpo no coincide con el "id" de la URL.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        item = self._find_item(item_id)
        if not item:
            return Response(
                {'message': f'No se encontró un elemento con id={item_id}.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if 'name' not in data or 'email' not in data:
            return Response(
                {'message': 'PUT requiere los campos "name" y "email" para reemplazo completo.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        item['name'] = data.get('name')
        item['email'] = data.get('email')

        if 'is_active' in data:
            item['is_active'] = bool(data.get('is_active'))

        return Response(
            {'message': 'Elemento actualizado completamente (PUT).', 'data': item},
            status=status.HTTP_200_OK
        )

    def patch(self, request, item_id):
        data = request.data

        item = self._find_item(item_id)
        if not item:
            return Response(
                {'message': f'No se encontró un elemento con id={item_id}.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if 'id' in data and str(data.get('id')) != str(item_id):
            return Response(
                {'message': 'No se permite modificar el "id" del elemento.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        updated = False

        if 'name' in data:
            item['name'] = data.get('name')
            updated = True

        if 'email' in data:
            item['email'] = data.get('email')
            updated = True

        if 'is_active' in data:
            item['is_active'] = bool(data.get('is_active'))
            updated = True

        if not updated:
            return Response(
                {'message': 'PATCH no recibió campos válidos para actualizar.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            {'message': 'Elemento actualizado parcialmente (PATCH).', 'data': item},
            status=status.HTTP_200_OK
        )

    def delete(self, request, item_id):
        item = self._find_item(item_id)
        if not item:
            return Response(
                {'message': f'No se encontró un elemento con id={item_id}.'},
                status=status.HTTP_404_NOT_FOUND
            )

        if item.get('is_active') is False:
            return Response(
                {'message': 'El elemento ya se encuentra eliminado (inactivo).'},
                status=status.HTTP_409_CONFLICT
            )

        item['is_active'] = False
        return Response(
            {'message': 'Elemento eliminado lógicamente (DELETE).', 'data': item},
            status=status.HTTP_200_OK
        )
