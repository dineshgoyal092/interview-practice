from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

STATUS = [
    ('Pending', 'pending'),
    ('InProgress','inprogress'),
    ('Resolved','resolved'),
    ('Cancelled','cancelled')
]

class Ticket(models.Model):
    query = models.TextField()
    created_by = models.ForeignKey(Agent, null=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    status = models.CharField(choices = STATUS, max_length=30)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    resolved_on = models.DateTimeField(null=True)

    def __str__(self):
        return f"(query={self.query}, customer {self.customer})"




# We provide health services to 20M+ users via coaches. User installs app, buys plan, chooses a trainer(yoga, dietitian) and starts their fitness journey..
#
# Now we need to build a customer support team which can help users with their concerns.
# Each customer support agent will have access to a web dashboard to note user queries & concerns.
#
# Requirements
# * Each support agent will have their own login credentials.
# * They  can search for a user based on email, first name.
# * They will get options to see any previous support ticket for the user with their information such as created date, current status, resolved date, user query etc
# * Agent will also have a form to create new support ticket for users. It will have user email & user question. If in search, user was available, the email is autofilled.
# * When this form is submitted, a new support ticket is created for this user with information such as user, email, query, status, created by, created on etc
#
# Tasks
# * Create tables to help satisfy above requirements.
# * Create API contracts & methods which will help in implementaion of the feature.
# APIs:
#
# GET /search_user?search_text=
# it can be firstname or email
#
# POST /ticket
# {
#     "query" :" ",
#     "user_id": ""
# }
# 201
#
# unathorised
# 401
# 400
# 500
#
# GET /tickets?user_id=
# return
# list of tickets
# [{
#
# }]
# success:
# 200
#
# error:
# 401
# 500
# 400
#
#
# create users in db directly
# create agent in db direclty

