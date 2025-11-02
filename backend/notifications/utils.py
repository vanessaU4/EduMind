"""Utility functions for creating and managing notifications"""
from django.utils import timezone
from datetime import timedelta
from .models import Notification, NotificationPreference


def create_notification(
    user,
    notification_type,
    title,
    message,
    priority='medium',
    action_url='',
    action_text='',
    metadata=None,
    expires_in_days=None
):
    """
    Create a notification for a user.
    
    Args:
        user: User instance
        notification_type: Type of notification (from NOTIFICATION_TYPES)
        title: Notification title
        message: Notification message
        priority: Priority level (default: 'medium')
        action_url: Optional URL for action button
        action_text: Optional text for action button
        metadata: Optional dict of additional data
        expires_in_days: Optional number of days until expiration
    
    Returns:
        Notification instance
    """
    expires_at = None
    if expires_in_days:
        expires_at = timezone.now() + timedelta(days=expires_in_days)
    
    notification = Notification.objects.create(
        user=user,
        notification_type=notification_type,
        title=title,
        message=message,
        priority=priority,
        action_url=action_url,
        action_text=action_text,
        metadata=metadata or {},
        expires_at=expires_at
    )
    
    return notification


def create_community_reply_notification(user, post_title, reply_author, post_id):
    """Create notification for community reply"""
    return create_notification(
        user=user,
        notification_type='community_reply',
        title='New Reply to Your Post',
        message=f'{reply_author} replied to your post "{post_title}"',
        priority='low',
        action_url=f'/community/post/{post_id}',
        action_text='View Post',
        metadata={'post_id': post_id}
    )


def create_assessment_reminder_notification(user, assessment_name):
    """Create notification for assessment reminder"""
    return create_notification(
        user=user,
        notification_type='assessment_reminder',
        title='Time for Your Mental Health Check-in',
        message=f'It\'s time to complete your {assessment_name} assessment',
        priority='medium',
        action_url='/assessments',
        action_text='Take Assessment',
        expires_in_days=7
    )


def create_crisis_alert_notification(user, message):
    """Create high-priority crisis alert notification"""
    return create_notification(
        user=user,
        notification_type='crisis_alert',
        title='Crisis Support Available',
        message=message,
        priority='urgent',
        action_url='/crisis-support',
        action_text='Get Help Now'
    )


def create_peer_match_notification(user, peer_name):
    """Create notification for peer match"""
    return create_notification(
        user=user,
        notification_type='peer_match',
        title='New Peer Match',
        message=f'You\'ve been matched with {peer_name} for peer support',
        priority='medium',
        action_url='/community/peers',
        action_text='View Profile'
    )


def create_achievement_notification(user, achievement_name, achievement_description):
    """Create notification for achievement"""
    return create_notification(
        user=user,
        notification_type='achievement',
        title='Achievement Unlocked!',
        message=f'{achievement_name}: {achievement_description}',
        priority='low',
        action_url='/profile/achievements',
        action_text='View Achievements'
    )


def should_send_notification(user, notification_type):
    """
    Check if a notification should be sent based on user preferences.
    
    Args:
        user: User instance
        notification_type: Type of notification to check
    
    Returns:
        Boolean indicating if notification should be sent
    """
    try:
        prefs = NotificationPreference.objects.get(user=user)
        
        # Check if in quiet hours
        if prefs.quiet_hours_start and prefs.quiet_hours_end:
            current_time = timezone.now().time()
            if prefs.quiet_hours_start <= current_time <= prefs.quiet_hours_end:
                # Allow urgent notifications even in quiet hours
                if notification_type == 'crisis_alert':
                    return True
                return False
        
        # Check type-specific preferences
        type_mapping = {
            'community_reply': prefs.community_notifications,
            'community_like': prefs.community_notifications,
            'assessment_reminder': prefs.assessment_reminders,
            'crisis_alert': prefs.crisis_alerts,
            'guide_message': prefs.guide_messages,
            'system_update': prefs.system_updates,
            'user_registration': prefs.user_registration_notifications,
            'user_approved': prefs.user_approval_notifications,
            'account_activated': prefs.account_activation_notifications,
        }
        
        return type_mapping.get(notification_type, True)
    
    except NotificationPreference.DoesNotExist:
        # If no preferences set, allow all notifications
        return True


def create_user_registration_notification(admin_user, new_user):
    """Create notification for admin when new user registers"""
    return create_notification(
        user=admin_user,
        notification_type='user_registration',
        title='New User Registration',
        message=f'New user {new_user.email} ({new_user.get_role_display()}) has registered and is pending approval',
        priority='medium',
        action_url=f'/admin/accounts/user/{new_user.id}/change/',
        action_text='Review User',
        metadata={'new_user_id': new_user.id, 'new_user_email': new_user.email}
    )


def create_user_approved_notification(user):
    """Create notification for user when their account is approved"""
    return create_notification(
        user=user,
        notification_type='user_approved',
        title='Account Approved - Welcome to eduMindSolutions!',
        message='Your account has been approved! You now have full access to the platform.',
        priority='high',
        action_url='/dashboard',
        action_text='Access Dashboard',
        metadata={'approval_date': user.approved_at.isoformat() if user.approved_at else None}
    )


def create_account_activated_notification(user):
    """Create notification for user when their account is activated"""
    return create_notification(
        user=user,
        notification_type='account_activated',
        title='Account Activated',
        message='Your account is now active and you can start using all platform features.',
        priority='medium',
        action_url='/profile',
        action_text='Complete Profile'
    )


def bulk_create_notifications(users, notification_type, title, message, **kwargs):
    """
    Create notifications for multiple users at once.
    
    Args:
        users: QuerySet or list of User instances
        notification_type: Type of notification
        title: Notification title
        message: Notification message
        **kwargs: Additional arguments for create_notification
    
    Returns:
        List of created Notification instances
    """
    notifications = []
    for user in users:
        if should_send_notification(user, notification_type):
            notification = create_notification(
                user=user,
                notification_type=notification_type,
                title=title,
                message=message,
                **kwargs
            )
            notifications.append(notification)
    
    return notifications
