from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from chat.models import Conversation  # Change if your model has a different name

class Command(BaseCommand):
    help = 'Delete conversations older than 30 days'

    def handle(self, *args, **kwargs):
        cutoff = timezone.now() - timedelta(days=30)
        deleted, _ = Conversation.objects.filter(created_at__lt=cutoff).delete()
        self.stdout.write(f'Deleted {deleted} old conversations.')
