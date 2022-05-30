from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
@permission_classes([])
def registerAV(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            account=serializer.save()

            data['response'] = 'Registration Successfully'
            data['username'] = account.username
            data['email'] = account.email

            refresh = RefreshToken.for_user(account)

            data['token'] = {
                'refresh': str(refresh),
                'access':str(refresh.access_token)
            }

