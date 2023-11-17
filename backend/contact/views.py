from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CONTACT
from .serializers import CONTACTSerializer

from rest_framework import generics


class Contact(generics.RetrieveAPIView):
    
    def post(self, request, *args, **kwargs):
        serializer = CONTACTSerializer(data=request.data)
        print(request.data)
        if request.data and serializer.is_valid():
            contactData = CONTACT.objects.create(
                email = request.data['email'],
                subject = request.data['subject'],
                message = request.data['message'],
                author = request.data.get('author', 'visitor')
            )
            contactData.save()
            return Response({'message': 'Message Saved'}, status.HTTP_202_ACCEPTED)
        return Response({'error': 'Error'}, status.HTTP_400_BAD_REQUEST)







# @api_view(['POST'])
# def contact(request):
#     try:
#         serializer = CONTACTSerializer(data=request.data)
#         print(request.data)
#         if request.data and serializer.is_valid():
#             contactData = CONTACT.objects.create(
#                 email = request.data['email'],
#                 subject = request.data['subject'],
#                 message = request.data['message'],
#                 author = request.data.get('author', 'visitor')
#             )
#             contactData.save()
#             return Response({'message': 'Message Saved', 'status': status.HTTP_202_ACCEPTED}, status=status.HTTP_202_ACCEPTED)
#         return Response({'message': 'Fill in the Required Fields', 'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({'error': e, 'status': status.HTTP_400_BAD_REQUEST}, status=status.HTTP_400_BAD_REQUEST)