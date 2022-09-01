from django.http.response import JsonResponse
from django.views.generic import TemplateView
from rest_framework.generics import (GenericAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from ckeditor_uploader.views import ImageUploadView as _ImageUploadView
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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['token'] = self.request.GET.get('token')
        return ctx

    def post(self, request, *args, **kwags):
        post = Post.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            user=request.user,
        )
        return JsonResponse({'id': post.id})


class ImageUploadAPIView(GenericAPIView, _ImageUploadView):
    pass
