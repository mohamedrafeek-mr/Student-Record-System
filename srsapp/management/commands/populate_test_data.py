from django.core.management.base import BaseCommand
from django.utils import timezone
from srsapp.models import User, Assignment


class Command(BaseCommand):
    help = 'Populate the database with test users and assignments'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing data before populating',
        )

    def handle(self, *args, **options):
        if options['clear']:
            User.objects.all().delete()
            Assignment.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing data'))

        # Create test users
        users_data = [
            {'username': 'john_doe', 'password': 'password123'},
            {'username': 'jane_smith', 'password': 'pass456'},
            {'username': 'alice_jones', 'password': 'alice789'},
        ]

        users = {}
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={'password': user_data['password']}
            )
            users[user_data['username']] = user
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created user: {user_data["username"]}'))
            else:
                self.stdout.write(f'User already exists: {user_data["username"]}')

        # Create assignments
        assignments_data = [
            {'username': 'john_doe', 'assignment_name': 'Python Project', 'submitted_status': 'Not Submitted'},
            {'username': 'john_doe', 'assignment_name': 'Django REST API', 'submitted_status': 'Submitted'},
            {'username': 'john_doe', 'assignment_name': 'Database Design', 'submitted_status': 'Not Submitted'},
            {'username': 'jane_smith', 'assignment_name': 'Web Development', 'submitted_status': 'Not Submitted'},
            {'username': 'jane_smith', 'assignment_name': 'JavaScript Basics', 'submitted_status': 'Submitted'},
            {'username': 'alice_jones', 'assignment_name': 'HTML & CSS', 'submitted_status': 'Not Submitted'},
            {'username': 'alice_jones', 'assignment_name': 'Vue.js Framework', 'submitted_status': 'Not Submitted'},
        ]

        for assign_data in assignments_data:
            user = users[assign_data['username']]
            submitted_time = timezone.now() if assign_data['submitted_status'] == 'Submitted' else None
            
            assignment, created = Assignment.objects.get_or_create(
                username=user,
                assignment_name=assign_data['assignment_name'],
                defaults={
                    'submitted_status': assign_data['submitted_status'],
                    'submitted_time': submitted_time
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created assignment: {assign_data["assignment_name"]} for {assign_data["username"]}'))
            else:
                self.stdout.write(f'Assignment already exists: {assign_data["assignment_name"]}')

        self.stdout.write(self.style.SUCCESS(f'\nTotal users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Total assignments: {Assignment.objects.count()}'))
