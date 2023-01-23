from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'userId', 'firstName', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            userId=validated_data['userId'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    userId = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        userId = data.get("userId", None)
        password = data.get("password", None)

        if User.objects.filter(userId=userId).exists():
            user = User.objects.get(userId=userId)
            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'userid': user.userId,
                    'firstName': user.firstName,
                    'access_token': access
                }

                return data
        else:
            raise serializers.ValidationError('존재하지 않는 사용자입니다.')
