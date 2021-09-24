from rest_framework import serializers
from .models import * 
import math

class ExtendedUserSerializer(serializers.Serializer):
    mobile = serializers.RegexField(regex=r'^[0-9]+$')
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

class ScreenSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    theater_id = serializers.IntegerField()
    no_of_seats = serializers.IntegerField()

    # def create(self, validate_data):
    #     name = validate_data.get('name')
    #     theater_id = validate_data.get('name')
    #     no_of_seats = validate_data.get('no_of_seats')
    #     theater = Theater.objects.get(id=theater_id)
    #     screen = Screen.objects.create(name=name, theater= theater, no_of_seats=no_of_seats)
    #     rows = math.ceil(no_of_seats / 5)
    #     cols = 5
    #     count = 0
    #     for row in range(rows):
    #         for col in range(cols):
    #             count += 1
    #             if count <= no_of_seats:
    #                 Seat.objects.create(row_no = row, col_no = col, screen= screen)
    #             else:
    #                 break
        

class MovieSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    duration_in_mins = serializers.CharField(max_length=200)

    class Meta:
        model = Movie
        fields = ("name","duration_in_mins")

    def create(self, validate_data):
        added_by = self.context.get('user')
        name = validate_data.get('name')
        duration_in_mins = validate_data.get('duration_in_mins')
        movie = Movie.objects.create(name=name,added_by=added_by, duration_in_mins=duration_in_mins)
        return movie


class ShowSerializer(serializers.ModelSerializer):
    slot = serializers.ChoiceField(choices = SLOT)
    movie_id = serializers.IntegerField()
    theater_id = serializers.IntegerField()
    price = serializers.IntegerField()
    date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Show
        fields = ("slot","movie_id","date","theater_id", "price", "screen_id")

    def create(self, validate_data):
        try:
            # import pdb
            # pdb.set_trace()
            slot = validate_data.get('slot')
            movie_id = validate_data.get('movie_id')
            date = validate_data.get('date')
            theater_id = validate_data.get('theater_id')
            booked_screens = Show.objects.filter(theater_id = theater_id, date= date, slot=slot).values('screen_id')
            print(booked_screens)
            screens = Screen.objects.filter(theater_id=theater_id)
            available_screen = None
            for i in screens:
                flag = False
                for j in booked_screens:
                    if i.id == j['screen_id']:
                        flag = True
                        break
                if not flag:
                    available_screen = i
                    break
            if not available_screen:
                raise Exception("no screen available")
            price = validate_data.get('price')
            # theater = Theater.objects.get(id=theater_id)
            # movie = Movie.objects.get(id=movie_id)
            show = Show.objects.create(slot=slot, theater_id= theater_id, movie_id=movie_id, date=date, screen=available_screen, price=price)
            
            rows = math.ceil(available_screen.no_of_seats / 5)
            cols = 5
            count = 0
            for row in range(rows):
                for col in range(cols):
                    count += 1
                    if count <= available_screen.no_of_seats:
                        Seat.objects.create(row_no = row, col_no = col, show= show)
                    else:
                        break
            return show
        except Exception as e:
            print(str(e))
            raise Exception(str(e))


class TransactionSerializer(serializers.Serializer):
    show_id = serializers.IntegerField()
    seat_ids = serializers.ListField(max_length=200)
    no_of_seats = serializers.IntegerField()

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ("__all__")
    
