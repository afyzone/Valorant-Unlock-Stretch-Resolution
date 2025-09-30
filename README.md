# Valorant Stretch Resolution Unlocker

This tool downloads a pre-configured `GameUserSettings.ini` file from GitHub and automatically places it into all the required Valorant **Config** directories on your system.  

---

## Instructions

### Step 1: Disable Monitors in Device Manager
1. Open **Device Manager**.  
2. Expand the **Monitors** section.  
3. Right-click each monitor listed and select **Disable device**.  
   - Do this for every monitor shown.  

*(This prevents Valorant from auto-detecting your display setup and overwriting settings.)*

---

### Step 2: Close Valorant
- Make sure Valorant is **completely closed** (not running in the background).  

---

### Step 3: Run the Script
1. Double-click `unlock_stretched_resolution.exe` (or run it in a terminal with `python unlock_stretched_res.py` for users running the source code).  
2. The script will:
   - Download the `GameUserSettings.ini` from GitHub.  
   - Copy it into every Valorant Config folder that requires it.  
   - Replace old versions if they exist.
