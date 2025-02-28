from django.db import models
from django.contrib.auth import get_user_model
from _base.models import BaseModel


User = get_user_model()

class Report(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return f"{self.user.email} - {self.title}"
