# Generated manually for chat media support

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_peersupportmatch_approved_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='message_type',
            field=models.CharField(choices=[('text', 'Text Message'), ('voice', 'Voice Message'), ('video', 'Video Message'), ('image', 'Image'), ('file', 'File'), ('system', 'System Message')], default='text', max_length=20),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='voice_file',
            field=models.FileField(blank=True, null=True, upload_to='chat/voice/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='chat/video/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='chat/images/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='attachment_file',
            field=models.FileField(blank=True, null=True, upload_to='chat/files/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='duration',
            field=models.PositiveIntegerField(blank=True, help_text='Duration in seconds for voice/video', null=True),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='file_size',
            field=models.PositiveIntegerField(blank=True, help_text='File size in bytes', null=True),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='mime_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='content',
            field=models.TextField(blank=True, help_text='Text content for text messages'),
        ),
    ]
