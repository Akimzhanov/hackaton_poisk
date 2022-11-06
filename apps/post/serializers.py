from rest_framework import serializers


from .models import (
    Lost,
    LostImage
)


class LostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = ('user', 'title', 'image', 'status', 'text', 'category', 'address', 'date' )


class LostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Lost
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['carousel'] = LostImageSerializer(
            instance.post_images.all(), many=True).data
        return representation


class LostImageSerializer(serializers.ModelSerializer):
     class Meta:
        model = LostImage
        fields = 'image',


class LostCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault(),
        source='user.username'
    )
    carousel_img = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )
    
    class Meta:
        model = Lost
        fields = '__all__'

    def create(self, validated_data):
        carousel_image = validated_data.pop('carousel_img')
        post = Lost.objects.create(**validated_data)
        images = []
        for image in carousel_image:
            images.append(LostImage(post=post, image=image))

        LostImage.objects.bulk_create(images)
        return post



