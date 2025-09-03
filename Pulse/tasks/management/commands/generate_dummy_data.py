from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from tasks.models import Task, TaskStatus, TaskPriority
from faker import Faker
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Generate dummy users, task statuses, priorities, and tasks"

    def add_arguments(self, parser):
        parser.add_argument("user_count", type=int, help="Number of users to create")
        parser.add_argument("task_count", type=int, help="Number of tasks to create")

    def handle(self, *args, **options):
        fake = Faker()
        user_count = options["user_count"]
        task_count = options["task_count"]

        # --- Create Users ---
        users = []
        for _ in range(user_count):
            username = fake.user_name()
            email = fake.email()
            user = User.objects.create_user(username=username, email=email, password="password123")
            users.append(user)
        self.stdout.write(self.style.SUCCESS(f"Created {user_count} fake users."))

        # --- Create TaskStatus ---
        status_names = ["Open", "In Progress", "Resolved", "Closed"]
        statuses = []
        for name in status_names:
            status, _ = TaskStatus.objects.get_or_create(name=name)
            statuses.append(status)
        self.stdout.write(self.style.SUCCESS(f"Ensured {len(status_names)} task statuses exist."))

        # --- Create TaskPriority ---
        priority_levels = [("Low", 1), ("Medium", 2), ("High", 3)]
        priorities = []
        for name, level in priority_levels:
            priority, _ = TaskPriority.objects.get_or_create(name=name, level=level)
            priorities.append(priority)
        self.stdout.write(self.style.SUCCESS(f"Ensured {len(priority_levels)} task priorities exist."))

        # --- Create Tasks ---
        for _ in range(task_count):
            Task.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.paragraph(nb_sentences=4),
                status=random.choice(statuses),
                priority=random.choice(priorities),
                created_by=random.choice(users),
                assigned_to=random.choice(users) if random.choice([True, False]) else None,
                due_date=fake.future_datetime(end_date="+30d"),
                is_resolved=random.choice([True, False]),
            )
        self.stdout.write(self.style.SUCCESS(f"Created {task_count} dummy tasks."))
