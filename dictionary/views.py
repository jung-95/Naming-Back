from .serializers import *
from .models import *
from rest_framework import views
from django.shortcuts import get_object_or_404
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from accounts.models import *
from urllib import parse


class dictionaryView(views.APIView):
    def get(self, request, pk, format=None):
        dictionarymake = get_object_or_404(dictionary, pk=pk)
        self.check_object_permissions(self.request, dictionarymake)
        serializer = dictionarySerializer(dictionarymake)
        return Response({'message': '사전 보여주기 성공', 'data': serializer.data}, status=HTTP_200_OK)


class dictionaryMakeView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        serializer = dictionarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '사전 만들기 성공', 'data': serializer.data}, status=HTTP_201_CREATED)
        return Response({'message': '사전 만들기 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class postListView(views.APIView):
    serializer_class = postSerializer

    def get_object(self, pk, format=None):
        postget = get_object_or_404(dictionary, pk=pk)
        return postget

    def get(self, request, pk):
        consonant = request.GET.get('consonant')
        params = {'consonant': consonant}
        arguments = {}
        for key, value in params.items():
            if value:
                arguments[key] = value

        postall = get_object_or_404(dictionary, pk=pk)

        postfilter = post.objects.filter(**arguments, dictionary=postall)

        serializer = self.serializer_class(postfilter, many=True)
        return Response({'message': '정의 보여주기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, pk):
        postmake = get_object_or_404(dictionary, pk=pk)
        serializer = postSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(dictionary=postmake)
            return Response({'message': '정의 적기 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '정의 적기 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class postDeleteView(views.APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk, format=None):
        postit = get_object_or_404(post, pk=pk)
        self.check_object_permissions(self.request, postit)
        return postit

    def delete(self, request, pk, post_pk):
        post = self.get_object(pk=post_pk)
        post.delete()
        return Response({'message': '정의 삭제 성공'}, status=HTTP_200_OK)


class postLikeView(views.APIView):
    serializer_class = postSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, post_pk):
        postmake = get_object_or_404(dictionary, pk=pk)
        post_like = get_object_or_404(post, pk=post_pk)
        post_like.is_liked = True
        post_like.likes += 1

        serializer = self.serializer_class(
            data=request.data, instance=post_like, partial=True)

        if serializer.is_valid():
            serializer.save(dictionary=postmake)
            return Response({'message': '정의 좋아요 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return Response({'message': '정의 좋아요 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, post_pk):
        post_like = get_object_or_404(post, pk=post_pk)
        post_like.is_liked = False
        post_like.likes -= 1

        serializer = self.serializer_class(
            data=request.data, instance=post_like, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': '정의 좋아요 취소 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return Response({'message': '정의 좋아요 취소 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class NicknameListView(views.APIView):
    serializer_class = NickNameSerializer

    def get_object(self, pk, format=None):
        getpost = get_object_or_404(dictionary, pk=pk)
        return getpost

    def get(self, request, pk):
        people = request.GET.get('nickname')
        params = {'nickname': people}
        arguments = {}
        for key, value in params.items():
            if value:
                arguments[key] = value

        postall = get_object_or_404(dictionary, pk=pk)

        postfilter = post.objects.filter(**arguments, dictionary=postall)

        serializer = self.serializer_class(postfilter, many=True)
        return Response({'message': '글쓴이 보여주기 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def post(self, request, pk):
        nicknamemake = get_object_or_404(dictionary, pk=pk)
        serializer = NickNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(dictionary=nicknamemake)
            return Response({'message': '닉네임 생성 성공', 'data': serializer.data}, status=HTTP_200_OK)
        return Response({'message': '닉네임 생성 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)


class SearchView(views.APIView):
    serializer_class = dictionaryListSerializer

    def get(self, request, **kwargs):
        keyword = request.GET.get('keyword')

        if request.GET.get(keyword)!=None:
            parse.unquote(request.GET.get(keyword))
        dictionarys = dictionary.objects.filter(firstName__contains=keyword)
        serializer = self.serializer_class(dictionarys, many=True)

        return Response({'message': '사전 검색 성공', 'data': serializer.data}, status=HTTP_200_OK)
