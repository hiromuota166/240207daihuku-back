from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import YourModel
from .serializers import YourModelSerializer

@api_view(['GET'])
def get_your_model(request):
    if request.method == 'GET':
        items = YourModel.objects.all()
        serializer = YourModelSerializer(items, many=True)
        return Response(serializer.data)
