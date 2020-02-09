from mates.models import *
from rest_framework.generics import ListAPIView,RetrieveAPIView
from .userserializer import UserListSerializer,RetrieveUserSerializer

class listUsers(ListAPIView):
    queryset = signup.objects.all()
    serializer_class = UserListSerializer


class RetrieveDetailsView(RetrieveAPIView):
    queryset = signup.objects.all()
    serializer_class = RetrieveUserSerializer