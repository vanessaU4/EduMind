# Generated manually for new notification preference fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_add_new_notification_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationpreference',
            name='user_registration_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notificationpreference',
            name='user_approval_notifications',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notificationpreference',
            name='account_activation_notifications',
            field=models.BooleanField(default=True),
        ),
    ]
