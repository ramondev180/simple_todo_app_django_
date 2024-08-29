from django.db import models

# Create your models here.

class TodoList(models.Model):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

    STATUS_CHOICES = [
        (IN_PROGRESS, "In progress"),
        (COMPLETED, "Completed")
    ]

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default=IN_PROGRESS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def status_html(self):
        status_classes = {
            'pending': 'badge bg-warning text-dark',
            'completed': 'badge bg-success text-light',
            'in_progress': 'badge bg-info text-light',
        }
        status_class = status_classes.get(self.status, 'badge bg-secondary text-light')
        return f"<span class='{status_class}'>{self.get_status_display()}</span>"

    def __str__(self) -> str:
        return self.title