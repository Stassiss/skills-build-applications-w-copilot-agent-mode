from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data for.'

    def handle(self, *args, **kwargs):
        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Alpha')
        team1.members.add(user1, user2)
        team2 = Team.objects.create(name='Team Beta')
        team2.members.add(user3)

        # Activities
        Activity.objects.create(user=user1, type='run', duration=30, date=timezone.now())
        Activity.objects.create(user=user2, type='walk', duration=45, date=timezone.now())
        Activity.objects.create(user=user3, type='cycle', duration=60, date=timezone.now())

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
