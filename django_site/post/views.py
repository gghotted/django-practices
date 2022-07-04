from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from post import serializers
from post.models import Post
from post.schema import common_parameters, common_responses, schemas


class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.PostCreateSerializer
        return serializers.PostSerializer

    @swagger_auto_schema(
        responses={
            200: schemas.posts,
        }
    )
    def get(self, request, *args, **kwargs):
        '''
        post list api 입니다.
        '''
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=schemas.post_create,
        responses={
            201: schemas.post_create_response,
            401: common_responses.response401,
        }
    )
    def post(self, request, *args, **kwargs):
        '''
        post create api 입니다.
        '''
        return super().post(request, *args, **kwargs)


class PostDetailUpdateDestroyAPIViewlAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return serializers.PostCreateSerializer
        return serializers.PostSerializer

    @swagger_auto_schema(
        manual_parameters=[
            common_parameters.id,
        ],
        responses={
            200: schemas.post,
            404: common_responses.response404,
        }
    )
    def get(self, request, *args, **kwargs):
        '''
        post detail api 입니다.
        '''
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            common_parameters.id,
        ],
        request_body=schemas.post_create,
        responses={
            200: schemas.post_create_response,
            401: common_responses.response401,
            404: common_responses.response404,
        }
    )
    def put(self, request, *args, **kwargs):
        '''
        post update api 입니다.
        '''
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            common_parameters.id,
        ],
        request_body=schemas.post_create,
        responses={
            200: schemas.post_create_response,
            401: common_responses.response401,
            404: common_responses.response404,
        }
    )
    def patch(self, request, *args, **kwargs):
        '''
        post update api 입니다.
        '''
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        manual_parameters=[
            common_parameters.id,
        ],
        responses={
            204: common_responses.response204,
            401: common_responses.response401,
            404: common_responses.response404,
        }
    )
    def delete(self, request, *args, **kwargs):
        '''
        post delete api 입니다.
        '''
        return super().delete(request, *args, **kwargs)


