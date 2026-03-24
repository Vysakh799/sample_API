from django.shortcuts import render

from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer
import csv

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'],url_path='upload-csv')
    def upload_csv(self,request):
        file = request.FILES.get('file')

        if not file:
            return Response({"error":"No file provided"},status=status.HTTP_400_BAD_REQUEST)
        elif not file.name.endswith('.csv'):
            return Response({"error":"Only CSV files are allowed"},status=status.HTTP_400_BAD_REQUEST)
        
        decFile = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decFile)

        success_count = 0 
        reject_count = 0
        errors = []

        for i,r in enumerate(reader,start = 1):
            serializer = UserSerializer(data = r)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')

                if User.objects.filter(email = email).exists():
                    reject_count +=1
                    errors.append({
                        'row':i,
                        "error":'Duplicate email skipped',
                        "data":r
                    })
                    continue
                serializer.save()
                success_count+=1

            else:
                reject_count += 1
                errors.append({
                    'row':i,
                    'error':serializer.errors,
                    'data':r                })
        return Response({
            'success_count':success_count,
            'rejected_count':reject_count,
            'errors':errors
        },status=status.HTTP_200_OK)
        