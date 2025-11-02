# Generated migration for enhanced forum comments with nested replies and likes

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        # Note: parent_comment -> parent rename is already handled in 0002_alter_chatroom_options_and_more.py
        # Note: reply_count field is already added in 0002_alter_chatroom_options_and_more.py
        # This migration is now empty as its operations were handled elsewhere
    ]
