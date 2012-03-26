from django.core.management.base import BaseCommand
from propaganda.utils import generate_pamphlets


class Command(BaseCommand):
    help = """
        Creates pamphlets with today's propaganda for active subscribers
        and queues them to mailer"""

    def handle(self, *args, **options):
        generate_pamphlets()

