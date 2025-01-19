from rest_framework.views import APIView
from rest_framework.response import Response

class ParcelListCreateView(APIView):
    def get(self, request):
        return Response({"message": "Protected API: List of parcels"})
