# Generated manually for user approval system

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_email_notifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=False, help_text='Admin approval status'),
        ),
        migrations.AddField(
            model_name='user',
            name='approved_at',
            field=models.DateTimeField(blank=True, help_text='When user was approved', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='approved_by',
            field=models.ForeignKey(blank=True, help_text='Admin who approved this user', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
