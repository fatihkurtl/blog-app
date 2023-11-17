from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import MEMBER, SocialMediaLink
from .serializers import MEMBERSerializer, SocialMediaLinkSerializer

import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from rest_framework import generics


KEY = '9eZ0fC3OhUaJvFATR7ifw6m2THrfC1dYfoQIWGK66i9JC9osWPKHZTRRY186kiy8'

@api_view(['POST'])
def signUp(request):
    print(request.data)
    serializer = MEMBERSerializer(data=request.data)
    if request.data and serializer.is_valid():
        encodedPassword = jwt.encode({'password': request.data['password']}, KEY, algorithm = 'HS256')
        
        member = MEMBER.objects.create(
            fullName=request.data['fullName'],
            userName=request.data['userName'],
            email=request.data['email'],
            profilePhoto=request.data['profilePhoto'],
            password=encodedPassword
        )
        member.save()
        return Response({'message': 'User Created Succesfully', 'status': status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    email = request.data['email']
    try:
        member = MEMBER.objects.get(email=email)
        serializer = MEMBERSerializer(member)

        if serializer.data['email']:
            decodedPassword = jwt.decode(serializer.data['password'], KEY, algorithms=['HS256'])
            
            if serializer.data['email'] == request.data['email'] and decodedPassword['password'] == request.data['password']:                
                expiration_time = datetime.utcnow() + timedelta(hours=1)
                token_payload = {
                    'user_id': serializer.data['userName'],
                    'exp': expiration_time,
                }
                SECRET_KEY = 'IsE6zk07Yhrtbl8voLPBR6AWzUMl9DOFo7QB0Sp6Aot3DY14zyzG0JPbyPIF5DZl'
                token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
                
                if member.tokenData == None:
                    member.tokenData = token
                    member.save()
                
                return Response({'message': 'Login Successful', 'token': member.tokenData, 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Wrong Email or Password', 'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    except MEMBER.DoesNotExist:
        return Response({'message': 'Wrong Email or Password', 'status': status.HTTP_404_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdateViewSet(generics.UpdateAPIView):
    
    def put(self, request, pk, *args, **kwargs):
        
        member = MEMBER.objects.filter(pk=pk).first()
        socialMediaLinks = SocialMediaLink.objects.filter(member=member.userName).first()
        print(socialMediaLinks)
        if member != None:
            if request.headers['Token'] == member.tokenData:
                member.fullName = request.data.get('fullName', member.fullName)
                member.email = request.data.get('email', member.email)
                member.profilePhoto = request.data.get('profilePhoto', member.profilePhoto)
                member.location = request.data.get('location', member.location)
                member.bio = request.data.get('bio', member.bio)
                member.save()
                
                if socialMediaLinks == None:
                    socialMediaLinks = SocialMediaLink(member=member)
                socialMediaLinks.x_url = request.data.get('x', socialMediaLinks.x_url)
                socialMediaLinks.github_url = request.data.get('github', socialMediaLinks.github_url)
                socialMediaLinks.linkedin_url = request.data.get('linkedin', socialMediaLinks.linkedin_url)
                socialMediaLinks.save()
                
                return Response({'message': 'Update Successful'}, status.HTTP_202_ACCEPTED)
            else:
                return Response({'message': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'User Not Found'}, status.HTTP_401_UNAUTHORIZED)


class DeleteMemberViewSet(generics.DestroyAPIView):
    
    def delete(self, request, pk, *args, **kwargs):
        
        member = MEMBER.objects.filter(pk=pk).first()
        if member != None:
            if request.headers['Token'] == member.tokenData:
                member.delete()
                return Response({'message': 'User deleted'}, status.HTTP_200_OK)
            else:
                return Response({'message': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'User Not Found'}, status.HTTP_400_BAD_REQUEST)


class SetPasswordViewSet(generics.UpdateAPIView):
    
    def put(self, request, pk, *args, **kwargs):
        
        member = MEMBER.objects.filter(pk=pk).first()
        if member != None:
            if request.headers['Token'] == member.tokenData:
                
                decodedPassword = jwt.decode(member.password, KEY, algorithms=['HS256'])                
                if request.data['currentPassword'] == decodedPassword['password']:
                    encodedPassword = jwt.encode({'password': request.data['password']}, KEY, algorithm = 'HS256')
                    member.password = encodedPassword
                    member.save()
                    return Response({'message': 'Password Changed Successful'}, status.HTTP_200_OK)
                else:
                    return Response({'message': 'Old Password Wrong'}, status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Unauthorized'}, status.HTTP_401_UNAUTHORIZED)
        return Response({'message': 'User Not Found'}, status.HTTP_400_BAD_REQUEST)


class ResetPasswordViewSet(generics.CreateAPIView):
    
    def post(self, request, *args, **kwargs):
        
        email = request.data['to']
        member = MEMBER.objects.filter(email=email).first()
        serializer = MEMBERSerializer(member)
        print(serializer.data)
        if serializer.data['email']:
            print(serializer.data['email'])
            message = f"""
                Dear {serializer.data['fullName']} - ({serializer.data['email']}),\n
                Click on the link below to securely reset your password:\n
                http://localhost:5173/new-password/member={serializer.data['tokenData']}\n
                Please do not share this link with others and keep your new password safe.\n
                Sincerely,
                fullstack.com team
            """
            emailw = EmailMessage(
                'Password Reset',
                message,
                settings.EMAIL_HOST_USER,
                [email]
            )
            emailw.send(fail_silently=False)
            return Response({'message': 'Email send successfully'}, status.HTTP_202_ACCEPTED)
        else:
            return Response({'message': 'This email is not in use'}, status.HTTP_400_BAD_REQUEST)



class NewPasswordViewSet(generics.UpdateAPIView):
    
    def put(self, request, *args, **kwargs):
        
        if 'Token' in request.headers:
            
            member = MEMBER.objects.filter(tokenData=request.headers['Token']).first()
            serializer = MEMBERSerializer(member)

            if serializer.data['tokenData'] == request.headers['Token']:
                encodedPassword = jwt.encode({'password': request.data['password']}, KEY, algorithm = 'HS256')
                member = MEMBER.objects.filter(tokenData=request.headers['Token']).update(password=encodedPassword) 
                return Response({'message': 'Password changed successfully'}, status.HTTP_201_CREATED)
            else:
                return Response({'status': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'status': status.HTTP_401_UNAUTHORIZED}, status=status.HTTP_401_UNAUTHORIZED)

    