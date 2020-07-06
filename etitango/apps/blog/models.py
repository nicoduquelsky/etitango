from django.db import models

# I keep this app cause will help us for paylments stuff.

class Blog(models.Model):
    Title = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        permissions = [
        ("deny_payload", "Can mark a payload as Denied"),
        ("confirm_payload", "Can mark a payload as confirmed"),
        ]
