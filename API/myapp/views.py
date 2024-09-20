from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from .models import StudentData
from .serializer import StudentSerializer

# Create your views here.
@api_view(['GET'])
def Get_API(request):
    mydata = StudentData.objects.all() # pylint: disable=no-member
    serializer = StudentSerializer(mydata, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def Post_API(request):
    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def Put_API(request,id):
    student = StudentData.objects.get(pk=id) # pylint: disable=no-member
    serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def Patch_API(request,id):
    student = StudentData.objects.get(pk=id) # pylint: disable=no-member
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)