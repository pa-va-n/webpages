from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

    class Meta:
        # This ensures Django creates a new table for your user, separate from the built-in user model
        db_table = 'custom_user'
        # Adding unique related_names for each relationship field to avoid clashes


    # Specify related_name in groups and user_permissions to something unique to avoid clash
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="user",
    )
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField(default='https://example.com/default-image.jpg')  # Ensure this field is defined if you are using URLs for images

    def __str__(self):
        return self.title
