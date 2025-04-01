import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Wait for database to become available"""
    
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        max_retries = 10
        delay_seconds = 2
        
        for i in range(max_retries):
            try:
                connections['default'].ensure_connection()
                self.stdout.write(self.style.SUCCESS('Database available!'))
                return
            except OperationalError:
                self.stdout.write(f'Attempt {i+1}/{max_retries}: Database unavailable, waiting...')
                time.sleep(delay_seconds)
        
        self.stdout.write(self.style.ERROR('Database never became available'))
        raise OperationalError("Database connection failed")