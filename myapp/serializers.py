from rest_framework import serializers
from myapp.models import NewUser, CreateSuggestioncomplaints


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'password', 'first_name',
                  'wilaya', 'commune', 'phonenumber')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SugSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = CreateSuggestioncomplaints
        fields = ('id', 'user', 'action', 'is_active')


class SugCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateSuggestioncomplaints
        fields = ('user', 'action', 'is_active')
