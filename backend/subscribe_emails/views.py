from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from member.models import MEMBER
from .models import SubscribeVisitors
from .serializers import SubscribeVisitorsSerializer


@api_view(['PUT'])
def email_subscribe(request):
    print(request.data)
    member = MEMBER.objects.filter(email=request.data['email']).first()
    print('member', member)
    if member:
        member.email_subscribe = True
        member.save()
    else:
        visitor = SubscribeVisitors(visitor_email=request.data['email']) 
        visitor.save()
    return Response({'message': 'Subscribed', 'status': status.HTTP_202_ACCEPTED}, status.HTTP_202_ACCEPTED)