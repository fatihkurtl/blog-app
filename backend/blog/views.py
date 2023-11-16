from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import POST, COMMENT, POST_LIKE, POST_SAVE

from member.models import MEMBER
from member.serializers import MEMBERSerializer

from .serializers import POSTSerializer, COMMENTSerializer, POST_LIKESerializer, POST_SAVESerializer

from .modules.pagination import PostsPagination
from rest_framework import viewsets

from urllib.parse import urlparse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation

from rest_framework import generics
from rest_framework import filters


def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = Response(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = Response("/")
    return response

class PostViewSet(generics.ListAPIView):
    queryset = POST.objects.all()
    serializer_class = POSTSerializer
    pagination_class = PostsPagination
    ordering_fields = ['-created_at']
    search_fields = ['title', 'subTitle', 'mdContent']
    filter_backends = (filters.SearchFilter,) # http://127.0.0.1:8000/api/blog/posts/?search=vue
    
    def get_queryset(self):
        print(self.kwargs)
        category = self.kwargs.get('category')        
        if category:
            return POST.objects.filter(is_active=True, category=category)
        return POST.objects.filter(is_active=True)
    
    # def get_serializer_context(self):
        # Serializer'a ek veri sağlamak için kullanılabilir
        # context = super().get_serializer_context()
        # context['extra_data'] = 'Some extra data'
        # return context
        
        
class PostDetailView(generics.RetrieveAPIView):
    queryset = POST.objects.all()
    serializer_class = POSTSerializer
    pk_url_kwarg = 'pk'
    category_url_kwarg = 'category'
    print(pk_url_kwarg)
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        print(self.get_object().category)
        print(self.request.method)
        serializer = self.get_serializer(instance)

        comments = COMMENT.objects.filter(post=instance, is_active=True)
        comment_serializer = COMMENTSerializer(comments, many=True)
        
        post_like = POST_LIKE.objects.filter(post=instance, is_liked=True)
        post_like_serializer = POST_LIKESerializer(post_like, many=True)
        print(post_like_serializer.data)
        
        post_save = POST_SAVE.objects.filter(post=instance, is_saved=True)
        post_save_serializer = POST_SAVESerializer(post_save, many=True)
        print(post_save_serializer.data)
        
        data = {
            'post': serializer.data,
            'comments': comment_serializer.data,
            # 'likes': post_like_serializer.data,
            'likes_count': len(post_like_serializer.data),
            # 'saves': post_save_serializer.data,
            'saves_count': len(post_save_serializer.data),
            'is_liked': False,
            'is_saved': False,
        }
            
        if 'Token' in request.headers:
            member = MEMBER.objects.filter(tokenData=request.headers['Token']).first()
            if member and member.tokenData == request.headers['Token']:
                is_liked = POST_LIKE.objects.filter(member=member.userName, post=self.get_object().id).first()
                is_saved = POST_SAVE.objects.filter(member=member.userName, post=self.get_object().id).first()
                if is_liked and is_liked.member.userName == member.userName:
                    data['is_liked'] = True
                if is_saved and is_saved.member.userName == member.userName:
                    data['is_saved'] = True
            else:
                return Response({'error': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)

        return Response(data, status.HTTP_200_OK)
    
    def post(self, request, pk, *args, **kwargs): # http://127.0.0.1:8000/api/blog/post/9/comment/
        # print(request.headers['Token'])
        if 'Token' not in request.headers:
            return Response({'message': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)
        member = MEMBER.objects.get(tokenData=request.headers['Token'])
        serializer = MEMBERSerializer(member)
        if request.headers['Token'] == serializer.data['tokenData']:
            post = POST.objects.get(pk=pk)
            print(post.title_tr)
            print(post.title_en)
            comment = COMMENT.objects.create(
                content=request.data['content'],
                member=member,
                post=post
            )
            comment.save()
            return Response({'message': 'Comment saved'}, status.HTTP_202_ACCEPTED)
        return Response({'message': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)
    
    def put(self, request, pk, *args, **kwargs):
        print(request.headers['Token'])
        print(request.data)
        if 'Token' not in request.headers:
            return Response({'message': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)
        return Response(request.data)
        
    
    
# http://127.0.0.1:8000/api/blog/posts/?page=2
# @api_view(['GET'])
# def allPosts(request):
#     try:
#         paginator = PostsPagination()
#         print(request.headers)
#         print(request.headers.get('Accept-Language', 'tr'))
#         posts = POST.objects.filter(is_active=True, language=request.headers.get('Accept-Language', 'tr')).order_by("-create_at")
#         result_page = paginator.paginate_queryset(posts, request)
#         if posts: 
#             serializer = POSTSerializer(result_page, many=True)
#             return paginator.get_paginated_response(serializer.data)
#     except POST.DoesNotExist:
#         return Response({'message': 'Posts Not Found', 'status': status.HTTP_204_NO_CONTENT})
#     return Response({'message': 'Posts Not Found', 'status': status.HTTP_204_NO_CONTENT})




# @api_view(['GET'])
# def postDetail(request, pk):
#     try:
#         post = POST.objects.get(pk=pk, is_active=True)
#         serializer = POSTSerializer(post)
#         comments = COMMENT.objects.filter(post=post)
#         commentSerializer = COMMENTSerializer(comments, many=True)
#         print(commentSerializer.data)
#         print(post)
#         return Response({'post': serializer.data, 'comments': commentSerializer.data}, status=status.HTTP_200_OK)
#     except POST.DoesNotExist:
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def categorizePosts(request, category):
#     try:
#         paginator = PostsPagination()
#         print(request.headers)
#         print(request.headers.get('Accept-Language', 'tr'))
#         posts = POST.objects.filter(is_active=True, category=category, language=request.headers.get('Accept-Language', 'tr'))
#         result_page = paginator.paginate_queryset(posts, request)
#         if posts:
#             serializer = POSTSerializer(result_page, many=True)
#             return paginator.get_paginated_response(serializer.data)
#         else: 
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     except POST.DoesNotExist:
#         return Response(status=status.HTTP_204_NO_CONTENT)

    
# @api_view(['GET'])
# def categorizeDetail(request, category, pk):
#     try:
#         post = POST.objects.get(is_active=True, category=category, pk=pk)
#         comments = COMMENT.objects.filter(post=post)
#         serializer = POSTSerializer(post)
#         commentSerializer = COMMENTSerializer(comments, many=True)
#         return Response({'post': serializer.data, 'comments': commentSerializer.data}, status=status.HTTP_200_OK)
#     except POST.DoesNotExist:
#         return Response(status=status.HTTP_204_NO_CONTENT)


# ! comment create api buraya bu api'yi yazmak icin gerekli kosul ve bilgiler notion da var
# @api_view(['POST']) # ? http://127.0.0.1:8000/api/post/2/comment/
# def createComment(request, pk):
#     try:
#         if request.headers['Token']:
#             member = MEMBER.objects.get(tokenData=request.headers['Token'])
#             serializer = MEMBERSerializer(member)
#             if request.headers['Token'] == serializer.data['tokenData']:
#                 print('member', serializer.data['userName'])
#                 print('kullaci yorum yapti')
#                 member = MEMBER.objects.get(tokenData=request.headers['Token'])
#                 post = POST.objects.get(pk=pk)
#                 print('member', member)         
#                 print('post', post)         
#                 comment = COMMENT.objects.create(
#                     content=request.data['content'],
#                     member=member,
#                     post=post
#                 )
#                 comment.save()
#                 return Response({'message': 'Comment saved', 'status': status.HTTP_202_ACCEPTED}, status=status.HTTP_202_ACCEPTED)
#     except ValueError as e:
#         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
