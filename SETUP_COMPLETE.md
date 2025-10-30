# 🎉 ClickUp Voice Tasks - Setup Complete!

## ✅ Current Status

- ✅ App files created
- ✅ OAuth credentials configured
- ✅ ngrok tunnel running
- ✅ Public URL active
- ✅ Timezone support added
- ✅ Date/time extraction working

---

## 🌐 Your Public URLs

### ngrok Public URL
```
https://03c2ee7b2ea8.ngrok-free.app
```

**Important**: This URL changes when you restart ngrok. Keep ngrok running!

---

## 🔧 ClickUp App Configuration

### Add this Redirect URL to your ClickUp App Settings:

Go to: https://app.clickup.com/settings/apps

**Redirect URL:**
```
https://03c2ee7b2ea8.ngrok-free.app/auth/callback
```

### Your OAuth Credentials (Already Configured)
- ✅ Client ID: `H537EKVMT5T84PLU1FZE5ZPBSPGX69DP`
- ✅ Client Secret: Configured in `.env`
- ⚠️  **Update the redirect URL** in your ClickUp app to match ngrok URL above

---

## 📱 OMI App Configuration

### Use These URLs in OMI Developer Settings:

```
App Home URL:
https://03c2ee7b2ea8.ngrok-free.app/

Auth URL:
https://03c2ee7b2ea8.ngrok-free.app/auth

Webhook URL:
https://03c2ee7b2ea8.ngrok-free.app/webhook

Setup Completed URL:
https://03c2ee7b2ea8.ngrok-free.app/setup-completed
```

---

## 🎯 Trigger Phrases (4 options)

Your app responds to these phrases:

1. **"Create ClickUp task"**
   - Example: "Create ClickUp task fix login bug by tomorrow"

2. **"Create click up task"**
   - Example: "Create click up task update docs by Friday 5pm"

3. **"Add click up task"**
   - Example: "Add click up task review mockups in 2 hours"

4. **"Add ClickUp task"**
   - Example: "Add ClickUp task team meeting next Monday at 10am"

---

## 🚀 Starting the App

### 1. Install Dependencies (if not done)

```bash
cd /Users/aaravgarg/omi-ai/Code/apps/clickup

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install with trusted hosts (SSL workaround)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### 2. Run the App

```bash
# Make sure you're in the clickup directory with venv activated
python main.py
```

You should see:
```
✅ OMI ClickUp Tasks Integration
==================================================
✅ Using file-based storage
🚀 Starting on 0.0.0.0:8000
==================================================
```

### 3. Keep Both Running

- ✅ **ngrok**: Already running → `https://03c2ee7b2ea8.ngrok-free.app`
- ⏳ **Python app**: Start with command above → `http://localhost:8000`

---

## 🧪 Test the App

### Test Interface

Visit: **https://03c2ee7b2ea8.ngrok-free.app/test?dev=true**

1. Click **"Authenticate ClickUp"**
2. Complete OAuth flow
3. Try example commands
4. Watch tasks being created!

### Test Commands

```
Create ClickUp task fix the login page bug by tomorrow 5pm

Add ClickUp task called update documentation by Friday

Create ClickUp task urgent meeting prep in 2 hours high priority
```

---

## 🌍 Timezone Setup (Important!)

After authenticating, **set your timezone**:

1. Go to: `https://03c2ee7b2ea8.ngrok-free.app/?uid=<your_uid>`
2. Scroll to **"🌍 Timezone Settings"**
3. Select your timezone (default is Pacific/Los Angeles)
4. Click **"Save Timezone"**

**Why?** This ensures dates like "tomorrow" and "Friday at 5pm" are calculated correctly for your location!

---

## 📊 How Segments Work

**OMI sends transcripts in segments** as you speak:

- ✅ Detects trigger phrase
- ✅ Collects up to **5 segments** OR stops after **5+ second gap**
- ✅ Silent during collection (no spam)
- ✅ AI processes all segments together
- ✅ One notification on completion

**Smart Collection:**
- **Max segments**: 5
- **Timeout**: 5 seconds of silence → processes immediately
- **Minimum**: 2 segments (trigger + content)
- **Duration**: ~5-20 seconds depending on speech

---

## 🧠 AI Extraction

The AI automatically identifies:

1. **List name** - Fuzzy matches to your workspace lists
2. **Task name** - Concise title
3. **Description** - Additional details
4. **Priority** - Urgent (1), High (2), Normal (3), Low (4)
5. **Due date** - Converts "tomorrow", "Friday 5pm", "in 2 hours" to actual dates in YOUR timezone

---

## 📝 Example Flow

```
You: "Create ClickUp task fix login bug by tomorrow 5pm"
     [collecting segment 1/5...]
     
You: "users can't sign in properly high priority"
     [collecting segment 2/5...]
     
     [5+ second pause - timeout!]
     → AI processes 2 segments

AI Extracts (in America/Los_Angeles timezone):
├─ List: UNKNOWN (will use default)
├─ Task: Fix login bug
├─ Description: Users can't sign in properly
├─ Priority: 2 (high)
└─ Due Date: 2025-10-31T17:00:00 (tomorrow at 5pm PST)

✅ Task created in ClickUp!
🔔 Notification: "Task created: Fix login bug"
```

---

## 🎨 Voice Examples with Dates

**Relative dates:**
```
"Create ClickUp task by tomorrow"
"Add ClickUp task in 3 hours"
"Create ClickUp task next week"
```

**Specific days:**
```
"Create ClickUp task by Friday"
"Add ClickUp task this Monday"
"Create ClickUp task next Wednesday"
```

**With times:**
```
"Create ClickUp task by 5pm today"
"Add ClickUp task tomorrow at 10am"
"Create ClickUp task Friday at 2:30pm"
```

**Combined:**
```
"Create ClickUp task urgent meeting tomorrow at 9am high priority"
"Add ClickUp task submit report by end of week"
"Create ClickUp task review code by Monday 3pm in bug tracker"
```

---

## ⚙️ Settings Page Features

Visit: **https://03c2ee7b2ea8.ngrok-free.app/?uid=<your_uid>**

1. **Default List** - Set a fallback list for tasks
2. **Refresh Lists** - Update list cache from ClickUp
3. **Timezone** - Select your timezone for accurate dates
4. **Logout** - Clear data and re-authenticate

---

## 🔍 What's Different from Original

### Before (Had Issues):
- ❌ AI used example dates from training data
- ❌ Dates could be in the past (one year ago)
- ❌ No timezone awareness
- ❌ "Tomorrow" could mean any date

### After (Fixed):
- ✅ AI receives current date/time context
- ✅ Dates always in the future (or current day)
- ✅ User selects timezone
- ✅ "Tomorrow" = actual tomorrow in user's timezone
- ✅ Timezone-aware date conversion
- ✅ Daylight saving handled automatically

---

## 🐛 Troubleshooting

### Wrong timezone?
→ Go to settings and update your timezone
→ AI uses this for all date calculations

### Dates still wrong?
→ Check app logs for AI extraction output
→ Verify timezone is saved (should show in settings)
→ Try re-authenticating

### Task created without due date?
→ AI might not have detected date/time in command
→ Try being more explicit: "by tomorrow" or "next Friday"
→ Check logs to see what AI extracted

---

## 🎉 Ready to Use!

1. ✅ **ngrok running**: https://03c2ee7b2ea8.ngrok-free.app
2. ⏳ **Start Python app**: `python main.py`
3. ⏳ **Update ClickUp redirect URL** (see above)
4. ⏳ **Configure OMI app** (see URLs above)
5. ⏳ **Set your timezone** in app settings
6. ⏳ **Test it**: "Create ClickUp task test by tomorrow"

---

## 💡 Pro Tips

- 🌍 **Set timezone first** - Before creating tasks with dates
- 🗣️ **Be specific** - "tomorrow 5pm" is better than just "tomorrow"
- ⏰ **Use natural language** - "in 2 hours", "next Friday", "end of week"
- 🎯 **Mention priority** - "urgent", "high priority", "low priority"
- 📋 **Specify list** - "in bug tracker", "to tasks list"

---

**Your ClickUp voice task creator is ready with accurate date/time support!** 🎤✅📅

