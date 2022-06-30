from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from post import serializers
from post.models import Post


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.PostCreateSerializer
        return serializers.PostSerializer


class PostDetailUpdateDestroyAPIViewlAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return serializers.PostCreateSerializer
        return serializers.PostSerializer

