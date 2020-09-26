import os
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
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


    def create(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': True})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class GetInTouch(viewsets.ModelViewSet):
    serializer_class = serializers.GetInTouchSerializer
    queryset = models.GeTInTouch.objects


    def create(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response({'message': 'response saved'})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



class BookTrial(viewsets.ModelViewSet):
    serializer_class = serializers.BookFreeTrialSerializer
    queryset = models.BookAFreeTrial.objects

    def create(self,request):
        data = request.data['register']
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'message': True})


@csrf_exempt
@api_view(['GET', 'POST'])
def payment(request):
    if (request.method == "POST"):
        data = request.data
        name = data['name']
        amount = data['amount']
        client = razorpay.Client(auth=("rzp_live_0RdkjhtdlQnks7", "PBtCT5r7OVpJrEiV9QhQMMlH"))
        order_id = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return Response({"name": name,"order_id":order_id['id']})



@csrf_exempt
@api_view(['GET', 'POST'])
def verifySignature(request):
    if (request.method == "POST"):
        data = request.data
        client = razorpay.Client(auth=("rzp_live_0RdkjhtdlQnks7", "PBtCT5r7OVpJrEiV9QhQMMlH"))
        params_dict = {
            'razorpay_order_id': data['order_id'],
            'razorpay_payment_id': data['payment_id'],
            'razorpay_signature': data['signature']
        }

        client.utility.verify_payment_signature(params_dict)
    return Response({"message":True})

@api_view(['GET','POSt'])

def send(request):
    data = request.data
    name = data['name']
    email = data['email']
    amount = data['amount']
    order_id = data['order_id']
    subject, from_email, to = 'Hello '+name, 'kalamlabs123@gmail.com', email
    text_content = 'Congrats, For the Registration of kalam labs'
    html_content = '<p>Your journey aboard with Kalam Labs has Begun. We shall be sending you more details by 08:00 AM/PM. <p>Your payment of Rs 799/- is successful</p><p>Your Transaction ID is: '+order_id+'</p>'
    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype='html'
    msg.attach_file('C:\elixirbackend\kalamlabs\kalamlabs.pdf')


    # f.close()
    msg.send()
    return Response({'message':'mail sent'})






