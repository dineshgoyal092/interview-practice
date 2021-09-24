from django.db import models
from django.contrib.auth.models import User

SLOT = [
    ('Morning', 'morning'),
    ('Noon', 'noon'),
    ('Evening', 'evening'),
    ('Night', ' night'),
]

# Create your models here.
class ExtendedUser(models.Model):
    user = models.ForeignKey(User,unique=True,on_delete=models.CASCADE, null=False, blank=False)
    mobile =  models.CharField(max_length=12,null=True)

    def __str__(self):
        return str(self.user)


class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Theater(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50)
    admin = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, null=False, default=1)

    def __str__(self):
        return self.name


class Screen(models.Model):
    name = models.CharField(max_length=50)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, null=False)
    no_of_seats = models.IntegerField(max_length=4)

    def __str__(self):
        return f"({self.name} {self.theater})"

class Movie(models.Model):
    name = models.CharField(max_length=50)
    duration_in_mins = models.IntegerField(max_length=3)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Show(models.Model):
    slot = models.CharField(max_length=20, choices=SLOT, null=False, blank=False)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField()
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    price = models.IntegerField(max_length=4)

    def __str__(self):
        return f"({self.movie} {self.date} {self.screen} {self.slot})"


class Seat(models.Model):
    row_no = models.IntegerField(max_length=2)
    col_no = models.IntegerField(max_length=2)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"({self.row_no} {self.col_no} {self.show_id})"

class Transaction(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.ManyToManyField('Seat')
    no_of_seats = models.IntegerField(max_length=2)
    date = models.DateTimeField()
    user_id = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    STATUS = [
        ('SUCCESS', 'success'),
        ('CANCELLED', 'cancelled'),
        ('IN-PROGRESS', 'in-progress'),
        ('Refunded', ' refunded'),
        ('Expired', ' expired'),
    ]
    status = models.CharField(max_length=20, choices=STATUS, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    

class GuestDetail(models.Model):
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    transaction = models.ForeignKey(Transaction, null=True, blank=True, on_delete=models.deletion.PROTECT)
    
class UnAvailableSeats(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, null=True, blank=True, on_delete=models.deletion.PROTECT)
    is_booked = models.BooleanField(default=False)
    release_time = models.DateTimeField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


