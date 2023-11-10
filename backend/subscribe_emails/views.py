from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from member.models import MEMBER
from .models import SubscribeVisitors
from .serializers import SubscribeVisitorsSerializer


@api_view(['PUT'])
def email_subscribe(request):
  """Subscribes a user to the newsletter."""

  email = request.data["email"]

  member = MEMBER.objects.filter(email=email).first()
  visitor = SubscribeVisitors.objects.filter(visitor_email=email).first()

  if member is not None and member.email == request.data['email']:
    member.email_subscribe = True
    member.save()
    return Response({'message': 'Subscribed', 'status': status.HTTP_202_ACCEPTED}, status.HTTP_202_ACCEPTED)

  visitor = SubscribeVisitors(visitor_email=email)
  visitor.save()
  return Response({'message': 'Subscribed', 'status': status.HTTP_202_ACCEPTED}, status.HTTP_202_ACCEPTED)