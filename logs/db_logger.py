from logging import Handler

class DBLogHandler(Handler):
    def emit(self, record):
        from .models import Log
        Log.objects.create(level=record.levelname, message=record.getMessage())