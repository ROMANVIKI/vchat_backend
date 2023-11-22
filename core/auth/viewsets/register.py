from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers.register import RegisterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        # Check if the serializer is valid without raising an exception
        if not serializer.is_valid():
            # Handle the invalid serializer case, e.g., return a response with error details
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response({
            "user": serializer.data,
            "refresh": res['refresh'],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)
























    #old code 

    # def create(self, request, *args, **kwargs):
    #     serializer = self.serializer_class(data=request.data)

    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     refresh = RefreshToken.for_user(user)
    #     res = {
    #         "refresh": str(refresh),
    #         "access": str(refresh.access_token),
    #     }
    #     return Response({
    #         "user": serializer.data,
    #         "refresh": res['refresh'],
    #         "token": res["access"]


    #     }, status=status.HTTP_201_CREATED)