from rest_framework import pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from .models import Post
from .serializers import ReadPostSerializer, WritePostSerializer


class PostsView(APIView):

    """Posts list view"""

    def get(self, request):
        paginator = LimitOffsetPagination()
        pagination.default_limit = 30
        posts = Post.objects.all()
        results = paginator.paginate_queryset(posts, request)
        serializer = ReadPostSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = WritePostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(author=request.user)
            post_serializer = ReadPostSerializer(post).data
            return Response(data=post_serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):

    """Post detail view"""

    def get_post(self, pk):

        """find post with pk and return post object

        :param: pk
        :return: Post
        """

        try:
            post = Post.objects.get(pk=pk)
            return post
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_post(pk)
        if post:
            serializer = ReadPostSerializer(post).data
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        post = self.get_post(pk)
        if post:
            if post.author != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer = WritePostSerializer(post, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(ReadPostSerializer(post).data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        post = self.get_post(pk)
        if post:
            if post.author != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            post.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
