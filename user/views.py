from .models import UserAccount
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


class UserView(APIView):
  def get(self, request):
    users = UserAccount.objects.all()
    return Response({"description": users})