from rest_framework import serializers

from post.models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
        )

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Post.objects.create(**validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
