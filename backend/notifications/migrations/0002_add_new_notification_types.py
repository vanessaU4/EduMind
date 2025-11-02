# Generated manually for new notification types

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        # This migration adds the new notification types to the model choices
        # The actual field choices are defined in the model, so no database changes needed
        # This is just for tracking the addition of new notification types:
        # - user_registration
        # - user_approved  
        # - account_activated
    ]
