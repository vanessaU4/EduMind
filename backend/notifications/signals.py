"""
Signal handlers for automatic notification creation
These signals can be connected to create notifications automatically when certain events occur
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .utils import (
    create_notification, should_send_notification, 
    create_user_registration_notification, create_user_approved_notification
)
from .email_utils import (
    send_user_registration_notification_to_admin,
    send_user_approval_notification,
    send_admin_user_approved_notification
)


# Example: Create notification when a user completes an assessment
# Uncomment and adjust based on your Assessment model
"""
@receiver(post_save, sender='assessments.AssessmentResult')
def notify_assessment_completed(sender, instance, created, **kwargs):
    if created and instance.user:
        if should_send_notification(instance.user, 'achievement'):
            create_notification(
                user=instance.user,
                notification_type='achievement',
                title='Assessment Completed!',
                message=f'You completed the {instance.assessment.name} assessment.',
                priority='low',
                action_url=f'/assessments/results/{instance.id}',
                action_text='View Results'
            )
"""


@receiver(post_save, sender='accounts.User')
def notify_user_registration(sender, instance, created, **kwargs):
    """Send notifications when a new user registers"""
    if created:
        # Send email notification to admin
        send_user_registration_notification_to_admin(instance)
        
        # Create in-app notification for admin users
        from accounts.models import User
        admin_users = User.objects.filter(role='admin', is_active=True)
        for admin in admin_users:
            if should_send_notification(admin, 'user_registration'):
                create_user_registration_notification(admin, instance)


@receiver(post_save, sender='accounts.User')
def notify_user_approval(sender, instance, created, **kwargs):
    """Send notifications when a user is approved"""
    if not created and instance.is_approved:
        # Check if this is a new approval (not just an update)
        if hasattr(instance, '_state') and instance._state.adding is False:
            try:
                # Get the previous state from database
                old_instance = sender.objects.get(pk=instance.pk)
                if hasattr(old_instance, 'is_approved') and not old_instance.is_approved:
                    # User was just approved
                    
                    # Send email notification to user
                    send_user_approval_notification(instance)
                    
                    # Create in-app notification for user
                    if should_send_notification(instance, 'user_approved'):
                        create_user_approved_notification(instance)
                    
                    # Send notification to admin about the approval
                    if instance.approved_by:
                        send_admin_user_approved_notification(instance, instance.approved_by)
                        
            except sender.DoesNotExist:
                # Handle case where old instance doesn't exist
                pass


# Example: Create notification when someone replies to a forum post
# Uncomment and adjust based on your Community models
"""
@receiver(post_save, sender='community.Comment')
def notify_post_reply(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        # Don't notify if user is replying to their own post
        if should_send_notification(instance.post.author, 'community_reply'):
            from .utils import create_community_reply_notification
            create_community_reply_notification(
                user=instance.post.author,
                post_title=instance.post.title,
                reply_author=instance.author.display_name,
                post_id=instance.post.id
            )
"""


# Example: Create notification for high-risk assessment results
"""
@receiver(post_save, sender='assessments.AssessmentResult')
def notify_high_risk_result(sender, instance, created, **kwargs):
    if created and instance.is_high_risk():
        from .utils import create_crisis_alert_notification
        create_crisis_alert_notification(
            user=instance.user,
            message='Based on your assessment, we recommend speaking with a crisis counselor.'
        )
        
        # Also notify assigned guides
        if hasattr(instance.user, 'assigned_guide') and instance.user.assigned_guide:
            create_notification(
                user=instance.user.assigned_guide,
                notification_type='crisis_alert',
                title='High-Risk Client Alert',
                message=f'Client {instance.user.display_name} has a high-risk assessment result.',
                priority='urgent',
                action_url=f'/clients/{instance.user.id}',
                action_text='View Client'
            )
"""


# Example: Create notification when a guide assigns an assessment
"""
@receiver(post_save, sender='assessments.AssessmentAssignment')
def notify_assessment_assigned(sender, instance, created, **kwargs):
    if created:
        from .utils import create_assessment_reminder_notification
        create_assessment_reminder_notification(
            user=instance.assigned_to,
            assessment_name=instance.assessment.name
        )
"""


# Example: Create notification for daily mood check-in reminders
def create_daily_mood_reminders():
    """
    This function can be called by a scheduled task (e.g., Celery, cron)
    to send daily mood check-in reminders
    """
    from accounts.models import User
    from datetime import datetime, timedelta
    
    # Get users who haven't logged mood today
    today = datetime.now().date()
    users_needing_reminder = User.objects.filter(
        is_active=True,
        role='user'
    ).exclude(
        last_mood_checkin__date=today
    )
    
    for user in users_needing_reminder:
        if should_send_notification(user, 'mood_checkin'):
            create_notification(
                user=user,
                notification_type='mood_checkin',
                title='Daily Mood Check-in',
                message='Take a moment to log how you\'re feeling today.',
                priority='low',
                action_url='/wellness/mood-tracker',
                action_text='Log Mood',
                expires_in_days=1
            )


# Example: Weekly wellness challenge notifications
def create_weekly_challenge_notifications():
    """
    This function can be called weekly to notify users about new challenges
    """
    from accounts.models import User
    
    active_users = User.objects.filter(is_active=True, role='user')
    
    for user in active_users:
        if should_send_notification(user, 'system_update'):
            create_notification(
                user=user,
                notification_type='system_update',
                title='New Weekly Challenge Available!',
                message='Check out this week\'s wellness challenge and earn rewards.',
                priority='low',
                action_url='/wellness/challenges',
                action_text='View Challenge',
                expires_in_days=7
            )
