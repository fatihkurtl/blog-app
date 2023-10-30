from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import POST, COMMENT

from member.models import MEMBER
from member.serializers import MEMBERSerializer

from .serializers import POSTSerializer, COMMENTSerializer

from .modules.pagination import PostsPagination
        
  
@api_view(['GET']) # http://127.0.0.1:8000/api/blog/posts/?page=2
def allPosts(request):
    try:
        paginator = PostsPagination()
        print(request.headers)
        print(request.headers.get('Accept-Language', 'tr'))
        posts = POST.objects.filter(is_active=True, language=request.headers.get('Accept-Language', 'tr')).order_by("-create_at")
        result_page = paginator.paginate_queryset(posts, request)
        if posts: 
            serializer = POSTSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
    except POST.DoesNotExist:
        return Response({'message': 'Posts Not Found', 'status': status.HTTP_204_NO_CONTENT})
    return Response({'message': 'Posts Not Found', 'status': status.HTTP_204_NO_CONTENT})


@api_view(['GET'])
def postDetail(request, pk):
    try:
        post = POST.objects.get(pk=pk, is_active=True)
        serializer = POSTSerializer(post)
        comments = COMMENT.objects.filter(post=post)
        commentSerializer = COMMENTSerializer(comments, many=True)
        print(commentSerializer.data)
        print(post)
        return Response({'post': serializer.data, 'comments': commentSerializer.data}, status=status.HTTP_200_OK)
    except POST.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def categorizePosts(request, category):
    try:
        paginator = PostsPagination()
        print(request.headers)
        print(request.headers.get('Accept-Language', 'tr'))
        posts = POST.objects.filter(is_active=True, category=category, language=request.headers.get('Accept-Language', 'tr'))
        result_page = paginator.paginate_queryset(posts, request)
        if posts:
            serializer = POSTSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else: 
            return Response(status=status.HTTP_204_NO_CONTENT)
    except POST.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['GET'])
def categorizeDetail(request, category, pk):
    try:
        post = POST.objects.get(is_active=True, category=category, pk=pk)
        comments = COMMENT.objects.filter(post=post)
        serializer = POSTSerializer(post)
        commentSerializer = COMMENTSerializer(comments, many=True)
        return Response({'post': serializer.data, 'comments': commentSerializer.data}, status=status.HTTP_200_OK)
    except POST.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)


# ! comment create api buraya bu api'yi yazmak icin gerekli kosul ve bilgiler notion da var
@api_view(['POST']) # ? http://127.0.0.1:8000/api/post/2/comment/
def createComment(request, pk):
    try:
        if request.headers['Token']:
            member = MEMBER.objects.get(tokenData=request.headers['Token'])
            serializer = MEMBERSerializer(member)
            if request.headers['Token'] == serializer.data['tokenData']:
                print('member', serializer.data['userName'])
                print('kullaci yorum yapti')
                member = MEMBER.objects.get(tokenData=request.headers['Token'])
                post = POST.objects.get(pk=pk)
                print('member', member)         
                print('post', post)         
                comment = COMMENT.objects.create(
                    content=request.data['content'],
                    member=member,
                    post=post
                )
                comment.save()
                return Response({'message': 'Comment saved', 'status': status.HTTP_202_ACCEPTED}, status=status.HTTP_202_ACCEPTED)
    except ValueError as e:
        return Response({'error': str(e)    }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
