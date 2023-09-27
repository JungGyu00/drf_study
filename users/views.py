from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.serializers import CustomTokenObtainPairSerializer, UserSerializer

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

from rest_framework import permissions


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


'''TokenObtainPairView 상송받아 커스터마이징하기'''


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class mockView(APIView):
    # 로그인되었는지 확인할 때 클래스형 뷰에서는 permission_classes를 만들어 줄수 있다.
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response("GET 요청")
