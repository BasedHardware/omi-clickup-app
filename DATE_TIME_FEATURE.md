# 📅 Date & Time Support for ClickUp Tasks

## ✨ New Feature Added

The ClickUp voice task creator now supports **due dates and times**! When you specify a date or time in your voice command, the AI will automatically extract it and set it as the task's due date in ClickUp.

---

## 🎤 How to Use

Simply include date/time information in your voice command:

### Examples

**Tomorrow:**
```
"Create ClickUp task fix the login bug by tomorrow"
→ Due date: Next day at 11:59 PM
```

**Specific day:**
```
"Add ClickUp task review design mockups before Friday"
→ Due date: This Friday at 11:59 PM
```

**With time:**
```
"Create ClickUp task meeting prep by 3pm today"
→ Due date: Today at 3:00 PM
```

**Relative time:**
```
"Add ClickUp task call client in 2 hours"
→ Due date: Current time + 2 hours
```

**Specific date:**
```
"Create ClickUp task submit report by January 15th"
→ Due date: January 15 at 11:59 PM
```

---

## 🧠 AI Detection

The AI understands various date/time formats:

### Relative Dates
- ✅ "tomorrow"
- ✅ "in 2 hours"
- ✅ "in 3 days"
- ✅ "next week"
- ✅ "next Friday"

### Specific Days
- ✅ "Monday"
- ✅ "this Friday"
- ✅ "next Tuesday"

### Specific Times
- ✅ "at 3pm"
- ✅ "by 5:30pm"
- ✅ "before noon"

### Specific Dates
- ✅ "January 15"
- ✅ "Jan 15th"
- ✅ "15th of January"

### Combined
- ✅ "Friday at 2pm"
- ✅ "tomorrow at 10am"
- ✅ "January 15th at 3:30pm"

---

## 📋 Complete Examples

### 1. **Bug Fix with Deadline**
```
"Create ClickUp task fix login page not loading in bug tracker by tomorrow 5pm high priority"
```
**AI Extracts:**
- List: bug tracker
- Task: Fix login page not loading
- Priority: High (2)
- Due Date: Tomorrow at 5:00 PM

### 2. **Meeting Reminder**
```
"Add ClickUp task prepare presentation slides before Friday 2pm"
```
**AI Extracts:**
- Task: Prepare presentation slides
- Due Date: This Friday at 2:00 PM
- Priority: Normal (3)

### 3. **Urgent Task with Time**
```
"Create ClickUp task urgent call client back in 30 minutes"
```
**AI Extracts:**
- Task: Call client back
- Priority: Urgent (1)
- Due Date: Current time + 30 minutes

### 4. **Long-term Task**
```
"Add ClickUp task submit quarterly report by March 31st"
```
**AI Extracts:**
- Task: Submit quarterly report
- Due Date: March 31 at 11:59 PM

---

## 🔧 Technical Details

### Date Format
The AI converts your spoken date/time into **ISO 8601 format**:
- Date only: `YYYY-MM-DD` (e.g., `2024-01-15`)
- Date + time: `YYYY-MM-DDTHH:MM:SS` (e.g., `2024-01-15T15:00:00`)

### ClickUp API
The system then converts ISO dates to **Unix timestamps in milliseconds** (ClickUp's required format).

### Default Time
If you specify a date without a time:
- Default is set to **11:59 PM** (end of day)
- Example: "tomorrow" → Tomorrow at 23:59:59

---

## 📝 What Changed

### Updated Files

1. **`task_detector.py`**
   - Added `DUE_DATE` extraction to AI prompt
   - Returns 6 values instead of 5: `(list_id, list_name, task_name, description, priority, due_date)`
   - AI examples updated to show date/time extraction

2. **`clickup_client.py`**
   - Added `due_date` parameter to `create_task()` method
   - Converts ISO date strings to Unix timestamps (milliseconds)
   - Handles both date-only and datetime formats

3. **`main.py`**
   - Updated all `ai_extract_task_details()` calls to receive `due_date`
   - Passes `due_date` to `create_task()` in all locations:
     - Test mode processing
     - Timeout monitor processing
     - Max segments processing

---

## ✅ Automatic Features

- **Smart Parsing**: Understands natural language dates/times
- **Timezone Aware**: Uses your system's timezone
- **Error Handling**: If date can't be parsed, task is still created (without due date)
- **Flexible Input**: Works with various date/time formats
- **No Due Date**: If no date mentioned, task created normally (no due date)

---

## 🎯 Priority Examples

### Without Date/Time
```
"Create ClickUp task fix bug in bug tracker high priority"
```
→ Task created with high priority, no due date

### With Date/Time
```
"Create ClickUp task fix bug in bug tracker by tomorrow high priority"
```
→ Task created with high priority AND due date (tomorrow at 11:59 PM)

---

## 🔄 Backward Compatibility

**Old commands still work!** If you don't mention a date/time:
```
"Create ClickUp task update documentation"
```
→ Works exactly as before (no due date set)

---

## 📊 Testing Examples

Try these in the test interface (`/test?dev=true`):

```
1. Create ClickUp task fix login bug by tomorrow
2. Add ClickUp task call client in 2 hours urgent
3. Create ClickUp task meeting prep Friday at 2pm
4. Add ClickUp task submit report by January 31st
5. Create ClickUp task review code before end of day
```

---

## 🎉 Benefits

- ⏰ **Never miss deadlines** - Set due dates with your voice
- 🗣️ **Natural language** - Speak dates like you normally would
- 🤖 **AI-powered** - Understands various date/time formats
- ✨ **Seamless** - Works alongside existing priority/description features
- 📅 **ClickUp integrated** - Due dates appear directly in ClickUp

---

**The date/time feature is now live! Start creating tasks with deadlines using your voice!** 🎤📅

