from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **options):
        # Clear existing data (delete individually to avoid Djongo ObjectId hashability issue)
        for model in [Activity, User, Team, Workout, Leaderboard]:
            for obj in model.objects.all():
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=date(2025, 1, 1))
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=date(2025, 1, 2))
        Activity.objects.create(user=users[2], type='swim', duration=60, date=date(2025, 1, 3))
        Activity.objects.create(user=users[3], type='run', duration=25, date=date(2025, 1, 4))

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        w2 = Workout.objects.create(name='Situps', description='Do 30 situps')
        w1.suggested_for.add(marvel)
        w2.suggested_for.add(dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
