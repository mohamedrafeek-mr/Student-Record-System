from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'


class Assignment(models.Model):
    SUBMISSION_STATUS_CHOICES = [
        ('Not Submitted', 'Not Submitted'),
        ('Submitted', 'Submitted'),
    ]
    
    assignment_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    assignment_name = models.CharField(max_length=255)
    submitted_status = models.CharField(max_length=50, choices=SUBMISSION_STATUS_CHOICES, default='Not Submitted')
    submitted_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.assignment_name} - {self.username}"
    
    class Meta:
        db_table = 'assignments'
