# ✅ ClickUp Voice Task Creator for OMI

Voice-activated ClickUp task creation through your OMI device. Simply say "Create ClickUp task" followed by your task details, and AI will automatically create it in the right list!

## ✨ Features

- **🎤 Voice-Activated** - Say "Create ClickUp task" and speak naturally
- **🧠 AI-Powered Task Extraction** - AI intelligently extracts task name, description, list, and priority
- **🔐 OAuth Authentication** - Secure ClickUp OAuth 2.0 integration
- **📋 List Selection** - Set a default list or specify in voice command
- **⚙️ Flexible Settings** - Change lists anytime from mobile-first homepage
- **🤖 Smart Extraction** - AI cleans up filler words and formats professionally
- **🔕 Silent Collection** - Only notifies when task is created
- **📱 Mobile-First UI** - Beautiful responsive ClickUp-themed design

## 🚀 Quick Start

### For OMI Users

1. **Install the app** in your OMI mobile app
2. **Authenticate** your ClickUp workspace (one-time)
3. **Select default list** (optional - you can specify in voice)
4. **Start creating tasks!**
   - Say: "Create ClickUp task fix login bug in bug tracker"
   - Say: "Add ClickUp task called update documentation"
   - Say: "Create ClickUp task review design mockups urgent priority"

### Trigger Phrases (4 options)

- **"create clickup task"** - "Create ClickUp task fix the login page"
- **"create click up task"** - "Create click up task update docs"
- **"add click up task"** - "Add click up task review mockups"
- **"add clickup task"** - "Add ClickUp task bug fix"

### How It Works

**The app intelligently processes your voice commands:**
1. Detects trigger phrase → Starts collecting
2. Collects up to 5 segments OR stops if 5+ second gap detected
3. AI extracts:
   - Task name/title
   - Task description (if provided)
   - List name (fuzzy matches to your workspace lists)
   - Priority (urgent=1, high=2, normal=3, low=4)
4. Fetches fresh list automatically
5. Creates task in ClickUp
6. Notifies you with confirmation! 🎉

**Example:**
```
You: "Create ClickUp task fix login page not loading in bug tracker"
     [collecting segment 1/5...]
You: "users can't sign in properly high priority"
     [collecting segment 2/5...]
     [5+ second pause - timeout!]
     → AI processes 2 segments
     
AI Extracted:
List: bug tracker
Task: Fix login page not loading
Description: Users can't sign in properly
Priority: 2 (high)

     → Task created! 🔔
```

## 🎯 OMI App Configuration

| Field | Value |
|-------|-------|
| **Webhook URL** | `https://your-app.up.railway.app/webhook` |
| **App Home URL** | `https://your-app.up.railway.app/` |
| **Auth URL** | `https://your-app.up.railway.app/auth` |
| **Setup Completed URL** | `https://your-app.up.railway.app/setup-completed` |

## 🛠️ Development Setup

### Prerequisites

- Python 3.10+
- ClickUp workspace with admin access
- OpenAI API key
- OMI device and app

### Installation

```bash
# Clone the repository
cd clickup

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Configuration

Create `.env` file with:

```env
# ClickUp OAuth Credentials (from app.clickup.com)
CLICKUP_CLIENT_ID=your_client_id
CLICKUP_CLIENT_SECRET=your_client_secret

# OAuth Redirect URL
OAUTH_REDIRECT_URL=http://localhost:8000/auth/callback

# OpenAI API Key (for AI task extraction)
OPENAI_API_KEY=your_openai_key

# App Settings
APP_HOST=0.0.0.0
APP_PORT=8000
```

### ClickUp App Setup

1. Go to [ClickUp Apps](https://app.clickup.com/settings/apps)
2. Click "Create an App"
3. Enter app name and details
4. Set redirect URL: `http://localhost:8000/auth/callback`
5. Copy Client ID and Client Secret to `.env`
6. Save the app

### Run Locally

```bash
source venv/bin/activate
python main.py
```

Visit `http://localhost:8000/test?dev=true` to test!

## ☁️ Railway Deployment

### Quick Deploy

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/omi-clickup-app.git
   git branch -M main
   git push -u origin main
   ```

2. **Deploy on Railway**
   - Go to [railway.app](https://railway.app)
   - New Project → Deploy from GitHub
   - Select your repo
   - Add environment variables (from your `.env`)

3. **Get your URL**
   - Settings → Networking → Generate Domain
   - You'll get: `your-app.up.railway.app`

4. **Update OAuth Redirect**
   - Railway Variables: `OAUTH_REDIRECT_URL=https://your-app.up.railway.app/auth/callback`
   - ClickUp App: Update redirect URL to same

5. **Configure OMI**
   - Use your Railway URLs in OMI app settings

### Railway Environment Variables

Add these in Railway dashboard:

```
CLICKUP_CLIENT_ID=your_client_id
CLICKUP_CLIENT_SECRET=your_client_secret
OPENAI_API_KEY=your_openai_key
OAUTH_REDIRECT_URL=https://your-app.up.railway.app/auth/callback
APP_HOST=0.0.0.0
APP_PORT=8000
PYTHONUNBUFFERED=1
```

**Note**: `PYTHONUNBUFFERED=1` ensures instant log output (no buffering delays)

## 🧪 Testing

### Web Interface

Visit `https://your-app.up.railway.app/test?dev=true` to:
- Authenticate your ClickUp workspace
- Test voice commands by typing
- See real-time logs
- Verify tasks are being created

### With OMI Device

1. Configure webhook URLs in OMI Developer Settings
2. Enable the integration
3. Authenticate ClickUp and select default list (optional)
4. Say: "Create ClickUp task fix the bug!"
5. Wait for AI processing (silent)
6. Get notification with confirmation! 🎉

## 🧠 AI Processing

The app uses OpenAI for intelligent processing:

1. **Task Name Extraction** - Extracts concise task title
2. **Description Extraction** - Captures additional details
3. **List Matching** - Fuzzy matches spoken list names to workspace lists
4. **Priority Detection** - Identifies urgency from keywords
5. **Cleanup** - Removes filler words, fixes grammar

**Example Transformation:**

```
Input (2 segments):
"fix the um login page bug in bug tracker it's like really urgent users can't sign in"

AI Output:
List: bug tracker (matched from "bug tracker")
Task: Fix login page bug
Description: Users can't sign in
Priority: 1 (urgent)
```

## 📊 How Segments Work

**OMI sends transcripts in segments** as you speak. The app:
- ✅ Detects trigger phrase (Create/Add ClickUp task)
- ✅ Collects up to 5 segments MAX
- ✅ Processes early if 5+ second gap detected (minimum 2 segments)
- ✅ Silent during collection (no spam)
- ✅ AI processes all collected segments together
- ✅ One notification on completion

**Smart Collection:**
- **Max segments:** 5 (including trigger)
- **Timeout:** 5 seconds of silence → processes immediately
- **Minimum:** 2 segments (trigger + content)
- **Duration:** ~5-20 seconds depending on speech

## 📱 List Management

### Specifying List in Voice

You can always specify the list in your voice command:
- "Create task in **bug tracker** called fix login"
- "Add task to **sprint planning** review mockups"
- "Create task **update docs** in documentation list"

AI will fuzzy match to your workspace lists!

### Using Default List

Set a default list in settings, then just say:
- "Create ClickUp task fix the bug"
- Task goes to your default list

### Refreshing List

The app caches your lists for performance. Click "Refresh Lists" button on homepage to update the cache.

## 🎨 Priority Levels

Mention priority in your voice command:
- **Urgent** (1) - "urgent task" or "critical priority"
- **High** (2) - "high priority" or "important"
- **Normal** (3) - Default if not specified
- **Low** (4) - "low priority" or "when you have time"

## 🔐 Security & Privacy

- ✅ OAuth 2.0 authentication (no password storage)
- ✅ Tokens stored securely with file persistence
- ✅ Per-user token isolation
- ✅ HTTPS enforced in production
- ✅ State parameter for CSRF protection

## 🐛 Troubleshooting

### "User not authenticated"
- Complete ClickUp OAuth flow
- Check Railway logs for auth errors
- Re-authenticate if needed

### "No list specified and no default list set"
- Visit app homepage
- Select a default list OR
- Specify list in voice command

### "Task not creating"
- Check Railway logs for errors
- Verify list exists and you have access
- Ensure ClickUp app has correct permissions
- Check ClickUp API rate limits

### "List not found"
- Check list name pronunciation
- AI does fuzzy matching but might need clearer speech
- Use "Refresh Lists" to update cache
- Set as default list in settings

### "Railway deployment fails"
- Verify all environment variables are set
- Check build logs for specific errors
- Ensure `OAUTH_REDIRECT_URL` matches ClickUp app

## 📁 Project Structure

```
clickup/
├── main.py                  # FastAPI application with mobile-first UI
├── clickup_client.py        # ClickUp API integration
├── task_detector.py         # AI-powered task extraction
├── simple_storage.py        # File-based storage (users & sessions)
├── requirements.txt         # Python dependencies
├── railway.toml            # Railway deployment config
├── runtime.txt             # Python version
├── Procfile                # Alternative deployment platforms
├── .env.example            # Environment template
├── .gitignore             # Git ignore rules
├── LICENSE                # MIT License
└── README.md              # This file
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage with list selection (mobile-first) |
| `/auth` | GET | Start ClickUp OAuth flow |
| `/auth/callback` | GET | OAuth callback handler |
| `/setup-completed` | GET | Check if user authenticated |
| `/webhook` | POST | Real-time transcript processor |
| `/update-list` | POST | Update selected default list |
| `/refresh-lists` | POST | Refresh list cache |
| `/logout` | POST | Logout and clear data |
| `/test` | GET | Web testing interface |
| `/health` | GET | Health check |

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing`)
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **OMI Docs**: [docs.omi.me](https://docs.omi.me)
- **ClickUp API**: [clickup.com/api](https://clickup.com/api)

## 🎉 Credits

Built for the [OMI](https://omi.me) ecosystem.

- **OMI Team** - Amazing wearable AI platform
- **ClickUp** - Productivity and task management platform
- **OpenAI** - Intelligent text processing

---

**Made with ❤️ for voice-first task management**

**Features:**
- 🎤 Voice-activated ClickUp task creation
- 🧠 AI-powered task extraction and list matching
- 📱 Mobile-first workspace management
- 🔐 Secure ClickUp OAuth integration
- ⚡ Real-time processing with Railway deployment

