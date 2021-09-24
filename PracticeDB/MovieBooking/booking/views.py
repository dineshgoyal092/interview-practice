from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status
from django.db.models import Q
import dateparser


class MovieView(APIView):
    """
    Create Movie API
    """
    serializer_class = serializers.MovieSerializer

    def post(self, request, format=None):
        user = request.user
        context = {
            "user":user
        }
        if not user.username or user.is_superuser is False:
            return Response({"status":"failed", "reason":"You dont have permission"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = serializers.MovieSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response({"movie":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status":"failed", "reason":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    # def get_all(self, request, format=None):
    #     user = request.user
    #     if not user.username:
    #         return Response({"status":"failed", "reason":"You dont have permission"}, status=status.HTTP_401_UNAUTHORIZED)
    #     movies = models.Movie.objects.all()
    #     serializer = serializers.MovieSerializer(movies, many=True)
    #     if serializer.is_valid():
    #         return Response({"movies":serializer.data}, status=status.HTTP_200_OK)
    #     return Response({"status":"failed", "reason":"unique constraint issue"}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk,format=None):
        user = request.user
        print(user)
        # pk = request.get('pk')
        if not user.username:
            return Response({"status":"failed", "reason":"You dont have permission"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            if pk == None:
                movies = models.Movie.objects.all()
                serializer = serializers.MovieSerializer(movies, many=True)
                if serializer.is_valid():
                    return Response({"movies":serializer.data}, status=status.HTTP_200_OK)
            else:
                movie = models.Movie.objects.get(id=pk)
                print(movie)
                serializer = serializers.MovieSerializer(movie)
                print(serializer)
                return Response({"movie":serializer.data}, status=status.HTTP_200_OK)
            # else:
            #     return Response({"status":"failed", "reason":"error in serialsation"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":"failed", "reason":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class ShowView(APIView):
    '''
    Show details
    '''

    serializer_class = serializers.ShowSerializer
    def post(self, request, format=None):
        user = request.user
        context = {
            "user":user
        }
        if not user.username or user.is_superuser is False:
            return Response({"status":"failed", "reason":"You dont have permission"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = serializers.ShowSerializer(data=request.data, context=context)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"show":serializer.data}, status=status.HTTP_201_CREATED)
            return Response({"status":"failed", "reason":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":"exception", "reason":str(e)}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, pk=None, movie_id= None, theater_id= None, date= None, format=None):
        try:
            if pk:
                show = models.Show.objects.get(id=pk)
                seats = models.Seat.objects.filter(show=show)
                
            movie_id = request.GET.get('movie_id')
            theater_id = request.GET.get('theater_id')
            date = request.GET.get('date')
            print(pk, movie_id, theater_id, date)
            q = Q()
            if movie_id:
                q &= Q(movie_id=movie_id)
            else:
                return Response({"status":"failed", "reason":"movie_id is mandatory filed"}, status=status.HTTP_400_BAD_REQUEST)
            if date:
                try:
                    date1 = dateparser.parse(date)
                    q &= Q(date__date=date)
                except Exception as e:
                    return Response({"status":"exception", "reason":str(e)}, status=status.HTTP_400_BAD_REQUEST)

            if theater_id:
                q &= Q(theater_id=theater_id)
            print(q)
            shows = models.Show.objects.filter(q)
            print(shows)
            serializer = serializers.ShowSerializer(shows, many=True)
            return Response({"shows":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"exception", "reason":str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SeatView(APIView):
    '''
    Show details
    '''

    serializer_class = serializers.SeatSerializer

    def get(self, request, show_id=None):

        print(show_id)
        seats = models.Seat.objects.filter(show_id=show_id)
        serializer = serializers.SeatSerializer(seats, many=True)
        return Response({"seats":serializer.data}, status=status.HTTP_200_OK)
    

def lock_seats(request):

    user = request.user
    context = {
        "user":user
    }
    if not user.username:
        return Response({"status":"failed", "reason":"Please login"}, status=status.HTTP_401_UNAUTHORIZED)
    
    seat_ids = request.POST['seat_ids']
    show_id = request.POST['show_id']
    
    



