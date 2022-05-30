from rest_framework import serializers
from .models import CustomUserModel

class UserSerializer(serializers.Serializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):

        password = self.validated_data.pop('password')
        print(password)
        password2 = self.validated_data.pop('password2')
        print(password2)

        if password != password2:
            raise serializers.ValidationError({'error':'p1 and p2 should be same'})

        if CustomUserModel.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email is already exists'})

        account = CustomUserModel(email = self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account
