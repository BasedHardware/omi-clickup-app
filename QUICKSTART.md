# 🚀 ClickUp Voice Tasks - Quick Start Guide

## ✅ Your App is Ready!

All files have been created and your ClickUp OAuth credentials are configured.

## 📋 Next Steps

### 1. Add Your OpenAI API Key

Edit the `.env` file and add your OpenAI API key:

```bash
# Open .env file and replace this line:
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Install Dependencies

```bash
cd /Users/aaravgarg/omi-ai/Code/apps/clickup

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Locally

```bash
# Make sure virtual environment is activated
python main.py
```

The app will start on `http://localhost:8000`

### 4. Test the App

Visit `http://localhost:8000/test?dev=true` in your browser to:
- Authenticate with ClickUp
- Test voice commands by typing
- See real-time logs
- Verify tasks are being created

### 5. Try These Commands

Once authenticated, try these example commands in the test interface:

```
Create ClickUp task fix the login page bug in bug tracker

Add ClickUp task called update documentation for API endpoints

Create ClickUp task review design mockups urgent priority
```

## 🎯 Trigger Phrases

Your app responds to these 4 trigger phrases:
- `create clickup task`
- `create click up task`
- `add click up task`
- `add clickup task`

## 🔧 ClickUp App Configuration

Your OAuth credentials are already configured:
- **Client ID**: H537EKVMT5T84PLU1FZE5ZPBSPGX69DP
- **Client Secret**: ✓ (configured)
- **Redirect URL**: http://localhost:8000/auth/callback

Make sure your ClickUp app settings match this redirect URL!

## 🎤 How to Use with OMI

### Example Voice Commands:

**Basic task creation:**
```
"Create ClickUp task fix the login bug"
```

**With list specified:**
```
"Create ClickUp task update docs in documentation list"
```

**With priority:**
```
"Add ClickUp task urgent priority fix critical bug in bug tracker"
```

**With description:**
```
"Create ClickUp task review design mockups before Friday meeting high priority"
```

## 📱 What the AI Extracts

The AI automatically identifies:
- **Task Name** - Concise title for the task
- **Description** - Additional details (if provided)
- **List** - Which list to create the task in (fuzzy match)
- **Priority** - Urgent (1), High (2), Normal (3), Low (4)

## 🎨 Example Flow

```
You: "Create ClickUp task fix login page not loading in bug tracker"
     [AI collecting...]
     
You: "users can't sign in properly high priority"
     [5 second pause - processing...]

AI Extracts:
├─ List: bug tracker
├─ Task: Fix login page not loading  
├─ Description: Users can't sign in properly
└─ Priority: 2 (high)

✅ Task created in ClickUp!
🔔 Notification: "Task created in bug tracker: Fix login page not loading"
```

## 🚀 Deploy to Railway (Optional)

When you're ready to deploy:

1. Push to GitHub
2. Connect to Railway
3. Add environment variables
4. Update redirect URL to your Railway domain
5. Configure OMI app with Railway URLs

See full instructions in [README.md](README.md)

## 🆘 Troubleshooting

### App won't start
- Make sure virtual environment is activated
- Check all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.10+)

### Authentication fails
- Verify ClickUp app redirect URL matches `.env` file
- Check OAuth credentials are correct
- Look at terminal logs for specific errors

### Tasks not creating
- Verify you're authenticated (test interface shows "Connected")
- Check the task name is at least 3 characters
- Ensure you have access to the target list
- Review terminal logs for API errors

## 📚 More Information

- **Full Documentation**: See [README.md](README.md)
- **ClickUp API Docs**: https://clickup.com/api
- **OMI Documentation**: https://docs.omi.me

---

**You're all set! Start the app and test it out! 🎉**

