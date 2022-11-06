from rest_framework import serializers

from .models import Find


class FindListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Find
        fields = ('user', 'title', 'image', 'status', 'text', 'category', 'address', 'date' )


class FindSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Find
        fields = '__all__'


class FindImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Find
        fields = 'image',


class FindCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )

    class Meta:
        model = Find
        fields = '__all__'
        
    def create(self, validated_data):
        post = Find.objects.create(**validated_data)
        return post
