from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serilazers, models
from rest_framework import status

class TicketView(APIView):

    serializer_class = serilazers.TicketSerialzer
    
    def post(self, request):
        user = request.user
        print(user.__dict__)
        if not user:
            Response({"status":"not authorised"}, status = status.HTTP_401_UNAUTHORIZED)
        if not user.is_staff:
            return Response({"status":"not authorised"}, status = status.HTTP_403_FORBIDDEN)
        context = {
            "agent_id": user.id
        }
        ticket_serialzer = serilazers.TicketSerialzer(data= request.data,context= context)
        
        if ticket_serialzer.is_valid():
            print("is_valid")
            ticket_serialzer.save()
            return Response({"stauts":"success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"stauts":ticket_serialzer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, customer_id=None):
        user = request.user
        print(request.__dict__)
        print(user.__dict__)
        if not user:
            Response({"status":"not authorised"}, status = status.HTTP_401_UNAUTHORIZED)
        if not user.is_staff:
            return Response({"status":"not authorised"}, status = status.HTTP_403_FORBIDDEN)
        print("customer", customer_id)
        tickets = models.Ticket.objects.filter(customer_id=customer_id)
        ticket_serialzer = serilazers.TicketSerialzer(tickets, many=True)
        return Response({"tickets":ticket_serialzer.data}, status=status.HTTP_200_OK)
        
        




        
        
    # def get(self, request,user_id):

