"""
OMI Notification Helper
Sends direct text notifications to OMI app users
"""
import os
import httpx
from typing import Optional

OMI_APP_ID = os.getenv("OMI_APP_ID")
OMI_APP_SECRET = os.getenv("OMI_APP_SECRET")


async def send_omi_notification(uid: str, message: str) -> bool:
    """
    Send a notification to an OMI user
    
    Args:
        uid: OMI user ID
        message: Notification message text
    
    Returns:
        bool: True if notification sent successfully, False otherwise
    """
    if not OMI_APP_ID or not OMI_APP_SECRET:
        print("⚠️  OMI credentials not configured, skipping notification", flush=True)
        return False
    
    if not uid or not message:
        print("⚠️  Missing uid or message for notification", flush=True)
        return False
    
    try:
        url = f"https://api.omi.me/v2/integrations/{OMI_APP_ID}/notification"
        headers = {
            "Authorization": f"Bearer {OMI_APP_SECRET}",
            "Content-Type": "application/json"
        }
        params = {
            "uid": uid,
            "message": message
        }
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(url, headers=headers, params=params)
            
            if response.status_code == 200:
                print(f"🔔 Notification sent to user {uid[:10]}...", flush=True)
                return True
            else:
                print(f"⚠️  Failed to send notification: {response.status_code} - {response.text}", flush=True)
                return False
                
    except Exception as e:
        print(f"❌ Error sending notification: {e}", flush=True)
        return False


async def notify_task_created(uid: str, task_name: str, list_name: str, due_date: Optional[str] = None) -> bool:
    """
    Send a task creation confirmation notification
    
    Args:
        uid: OMI user ID
        task_name: Name of the created task
        list_name: Name of the list where task was created
        due_date: Optional due date string (e.g., "Oct 31, 5pm")
    
    Returns:
        bool: True if notification sent successfully
    """
    if due_date:
        message = f"✅ Task created in {list_name}: {task_name} (Due: {due_date})"
    else:
        message = f"✅ Task created in {list_name}: {task_name}"
    
    return await send_omi_notification(uid, message)


async def notify_task_failed(uid: str, error: str) -> bool:
    """
    Send a task creation failure notification
    
    Args:
        uid: OMI user ID
        error: Error message
    
    Returns:
        bool: True if notification sent successfully
    """
    message = f"❌ Failed to create task: {error}"
    return await send_omi_notification(uid, message)

