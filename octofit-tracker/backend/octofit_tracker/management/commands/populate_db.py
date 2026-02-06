
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Drop collections directly using PyMongo for a clean slate
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db['leaderboard'].drop()
        db['activities'].drop()
        db['workouts'].drop()
        db['users'].drop()
        db['teams'].drop()


        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=captain, type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=batman, type='swim', duration=25, date=timezone.now().date())
        Activity.objects.create(user=superman, type='fly', duration=60, date=timezone.now().date())

        # Create workouts
        Workout.objects.create(name='Pushups', description='Do 3 sets of 15 pushups', suggested_for='all')
        Workout.objects.create(name='Sprints', description='5x100m sprints', suggested_for='marvel')
        Workout.objects.create(name='Deadlifts', description='3 sets of 10 deadlifts', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=captain, score=90)
        Leaderboard.objects.create(user=batman, score=95)
        Leaderboard.objects.create(user=superman, score=110)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
