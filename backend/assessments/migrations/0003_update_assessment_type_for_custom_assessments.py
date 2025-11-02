# Generated migration for custom assessment types

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assessments', '0002_add_assessment_requests_and_assignments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmenttype',
            name='name',
            field=models.CharField(help_text='Unique identifier for the assessment type', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='assessmenttype',
            name='total_questions',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='assessmenttype',
            name='max_score',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessmenttype',
            name='is_standard',
            field=models.BooleanField(default=False, help_text='True for standard assessments (PHQ9, GAD7, PCL5)'),
        ),
        migrations.AddField(
            model_name='assessmenttype',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='User who created this assessment type', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assessmenttype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        # Update existing standard assessments to mark them as standard
        migrations.RunSQL(
            "UPDATE assessments_type SET is_standard = TRUE WHERE name IN ('PHQ9', 'GAD7', 'PCL5');",
            reverse_sql="UPDATE assessments_type SET is_standard = FALSE WHERE name IN ('PHQ9', 'GAD7', 'PCL5');"
        ),
    ]
