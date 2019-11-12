from rest_framework.response import Response
from rest_framework.views import APIView
from users.api  import serializers as us

class CurrentUserAPIView(APIView):
    def get(self, request):
        serializer = us.UserDisplaySerializer(request.user)
        return Response(serializer.data)