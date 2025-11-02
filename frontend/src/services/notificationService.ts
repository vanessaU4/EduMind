import axios from 'axios';
import { authService } from './authService';
import type {
  Notification,
  NotificationPreference,
  NotificationListResponse,
  NotificationStats,
} from '@/types/notification';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// Create axios instance with auth token using authService
const getAuthHeader = () => {
  const token = authService.getAccessToken();
  return token ? { Authorization: `Bearer ${token}` } : {};
};

export const notificationService = {
  /**
   * Get all notifications for the current user
   */
  async getNotifications(page = 1, pageSize = 20): Promise<NotificationListResponse> {
    try {
      const response = await axios.get(
        `${API_BASE_URL}/notifications/`,
        {
          params: { page, page_size: pageSize },
          headers: getAuthHeader(),
        }
      );
      return response.data;
    } catch (error) {
      console.error('Error fetching notifications:', error);
      throw error;
    }
  },

  /**
   * Get unread notifications
   */
  async getUnreadNotifications(): Promise<NotificationListResponse> {
    try {
      const response = await axios.get(
        `${API_BASE_URL}/notifications/unread/`,
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error fetching unread notifications:', error);
      throw error;
    }
  },

  /**
   * Get a single notification by ID
   */
  async getNotification(id: number): Promise<Notification> {
    try {
      const response = await axios.get(
        `${API_BASE_URL}/notifications/${id}/`,
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error fetching notification:', error);
      throw error;
    }
  },

  /**
   * Mark a notification as read
   */
  async markAsRead(id: number): Promise<Notification> {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/notifications/${id}/mark_read/`,
        {},
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error marking notification as read:', error);
      throw error;
    }
  },

  /**
   * Mark all notifications as read
   */
  async markAllAsRead(): Promise<{ message: string; count: number }> {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/notifications/mark_all_read/`,
        {},
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error marking all notifications as read:', error);
      throw error;
    }
  },

  /**
   * Delete a notification
   */
  async deleteNotification(id: number): Promise<void> {
    try {
      await axios.delete(
        `${API_BASE_URL}/notifications/${id}/`,
        { headers: getAuthHeader() }
      );
    } catch (error) {
      console.error('Error deleting notification:', error);
      throw error;
    }
  },

  /**
   * Clear all read notifications
   */
  async clearAllRead(): Promise<{ message: string; count: number }> {
    try {
      const response = await axios.delete(
        `${API_BASE_URL}/notifications/clear_all/`,
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error clearing notifications:', error);
      throw error;
    }
  },

  /**
   * Get notification statistics
   */
  async getStats(): Promise<NotificationStats> {
    try {
      const response = await axios.get(
        `${API_BASE_URL}/notifications/stats/`,
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error fetching notification stats:', error);
      throw error;
    }
  },

  /**
   * Get notification preferences
   */
  async getPreferences(): Promise<NotificationPreference> {
    try {
      const response = await axios.get(
        `${API_BASE_URL}/notification-preferences/`,
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error fetching notification preferences:', error);
      throw error;
    }
  },

  /**
   * Update notification preferences
   */
  async updatePreferences(
    preferences: Partial<NotificationPreference>
  ): Promise<NotificationPreference> {
    try {
      const response = await axios.patch(
        `${API_BASE_URL}/notification-preferences/`,
        preferences,
        { headers: getAuthHeader() }
      );
      return response.data;
    } catch (error) {
      console.error('Error updating notification preferences:', error);
      throw error;
    }
  },
};
