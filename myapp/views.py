
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import generics
from myapp.models import CreateSuggestioncomplaints, NewUser


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Userlist(generics.ListAPIView):
    queryset = NewUser.objects.all()
    serializer_class = CustomUserSerializer


class PostList(generics.ListAPIView):
    queryset = CreateSuggestioncomplaints.objects.all()
    serializer_class = SugSerializer


class PostCreate(generics.CreateAPIView):
    queryset = CreateSuggestioncomplaints.objects.all()
    serializer_class = SugCreateSerializer


class PostDetail(generics.RetrieveDestroyAPIView):
    pass


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
