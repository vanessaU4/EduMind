# Generated migration for adding question types and options

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        # Add new fields to AssessmentQuestion
        migrations.AddField(
            model_name='assessmentquestion',
            name='question_type',
            field=models.CharField(
                choices=[
                    ('multiple_choice', 'Multiple Choice'),
                    ('multiple_select', 'Multiple Select'),
                    ('text_input', 'Text Input'),
                    ('rating_scale', 'Rating Scale'),
                    ('yes_no', 'Yes/No'),
                    ('likert_scale', 'Likert Scale'),
                ],
                default='multiple_choice',
                max_length=20
            ),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='is_required',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='min_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='max_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentquestion',
            name='scale_labels',
            field=models.JSONField(blank=True, null=True),
        ),
        
        # Create QuestionOption model
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('score', models.IntegerField()),
                ('order', models.PositiveIntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='assessments.assessmentquestion')),
            ],
            options={
                'db_table': 'assessments_question_option',
                'ordering': ['question', 'order'],
            },
        ),
        
        # Update AssessmentResponse model
        migrations.AddField(
            model_name='assessmentresponse',
            name='selected_option_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='assessments.questionoption'),
        ),
        migrations.AddField(
            model_name='assessmentresponse',
            name='selected_option_ids',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentresponse',
            name='text_response',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentresponse',
            name='numeric_response',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='assessmentresponse',
            name='response_value',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='assessmentresponse',
            name='response_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        
        # Remove old fields
        migrations.RemoveField(
            model_name='assessmentresponse',
            name='selected_option_index',
        ),
        migrations.RemoveField(
            model_name='assessmentresponse',
            name='score',
        ),
    ]
