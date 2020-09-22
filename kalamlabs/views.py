from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import models
from . import serializers
import razorpay
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.




class Register(viewsets.ModelViewSet):
    serializer_class = serializers.KalamRegistrationSerializer
    queryset = models.KalamRegistration.objects

    def list(self,request):

        return Response({'message':'hey i am working'})

    def create(self,request):
        data = request.data
        print(data)
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            a = self.queryset.filter(mobile__exact=serializer.validated_data['mobile']).first()
            return Response({'id': a.id})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self,request,pk=None):
        data = request.data
        name = data["name"]
        amount = data["amount"]
        client = razorpay.client(auth=("rzp_test_L3hv3powYQMGQn", "5QNSr9dG4LPu4IZ7c7rpnUM0"))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(data,pk)
        obj = self.queryset.get(pk=pk)
        obj.payment_amount=data['amount']
        obj.payment=True
        obj.save()
        return Response({'date': data['date'],'slot':data['slot']})


    def retrieve(self,request,pk=None):
        return Response({'http':'get'})



    def partial_update(self,request,pk=None):
        return Response({'http':'partial'})

    def destroy(self,request,pk=None):
        return Response({'http':'remove'})

@csrf_exempt
@api_view(['GET', 'POST'])
def payment(request):
    if (request.method == "POST"):
        data = request.data
        name = data['name']
        amount = data['amount']
        client = razorpay.Client(auth=("rzp_test_L3hv3powYQMGQn", "5QNSr9dG4LPu4IZ7c7rpnUM0"))
        order_id = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return Response({"name": name,"order_id":order_id['id']})






