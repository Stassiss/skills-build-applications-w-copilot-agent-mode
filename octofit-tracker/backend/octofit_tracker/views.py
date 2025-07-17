# API root with Codespace and localhost URLs
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    codespace_url = 'https://jubilant-yodel-pwgp6wrpg9vh7rx4-8000.app.github.dev/api/'
    localhost_url = 'http://localhost:8000/api/'
    return Response({
        'users': [codespace_url + 'users/', localhost_url + 'users/'],
        'teams': [codespace_url + 'teams/', localhost_url + 'teams/'],
        'activity': [codespace_url + 'activity/', localhost_url + 'activity/'],
        'leaderboard': [codespace_url + 'leaderboard/', localhost_url + 'leaderboard/'],
        'workouts': [codespace_url + 'workouts/', localhost_url + 'workouts/'],
    })
# Views for OctoFit collections
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
