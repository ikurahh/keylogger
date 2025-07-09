# Keylogger Script - Usage Guide

## 🧩 What This Script Does
- Records all keypresses in 3 different log files:
  - **Detailed log** with timestamps.
  - **Plaintext log** for actual typed sentences.
  - **Rotating structured log file**.
- Automatically stops after a set duration (default: 6000 seconds).
- Logs are stored in a **hidden folder**.

---

## 📁 Where Logs Are Stored
**Folder:**
```
C:\Users\<YourUsername>\$Recycle.Logs\
```

This folder is **hidden** by default. To access:
- Open File Explorer.
- Type: `%USERPROFILE%\$Recycle.Logs`
- Or enable **Hidden Items** in the View tab.

**Log Files:**
- `keylog_detailed.txt` → Timestamped key events.
- `keylogger_plaintext.txt` → Clean readable version.
- `keylogger_rfs.log` → Rotating logs with backups.

---

## 🚀 How to Use It

1. **Install Required Library**
   ```bash
   pip install pynput
   ```

2. **Run the Script**
   ```bash
   python keylogger.py
   ```

3. You will see:
   ```
   [INFO] Keylogger demo started. Logs are saved in a hidden folder.
   [INFO] Press Ctrl + C to stop manually or wait for auto-stop.
   ```

4. **Stop the Script**
   - Automatically after 6000 seconds.
   - Or manually with `Ctrl + C`.

---

## 🔐 Security Features
- Hidden logging folder.
- Rotating file stream (log management).
- Timestamped logs.
- Flushes buffer on shutdown.

---

## 📝 Metadata
- **Author:** Keylogger Demo Tool
- **Version:** 1.0
- **Log Session Start:** Auto-generated at runtime
