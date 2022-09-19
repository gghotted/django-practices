from django.http.response import JsonResponse
from django.views.generic import TemplateView
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


class PostCreateView(TemplateView):
    template_name = 'post/post_form.html'

    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return JsonResponse({'success': True})
