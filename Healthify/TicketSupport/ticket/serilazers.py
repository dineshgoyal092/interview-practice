from rest_framework import serializers
from .models import *

class TicketSerialzer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    query = serializers.CharField(max_length=100000)
    created_on = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)
    resolved_on = serializers.DateTimeField(required=False)
    #
    # class Meta:
    #     model = Ticket
    #     fields = ("query","status", "created_on", "customer_id")
        
    def create(self, validate_data):
        # print("inside_create")
        query = validate_data.get('query')
        print(validate_data, self.context)
        customer_id = int(validate_data.get('customer_id'))
        try:
            customer= Customer.objects.get(id=customer_id)
        except Exception as e:
            print(str(e))
            return e
        
        agent_id = self.context.get('agent_id')
        try:
            created_by= Agent.objects.get(user_id=agent_id)
            ticket = Ticket.objects.create(query=query, customer=customer, created_by=created_by, status='pending')
            print("successs")
            return ticket
        except Exception as e:
            print(str(e))
            return e
    