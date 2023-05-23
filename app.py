import random

import cv2
from flask import Flask, Response, render_template

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode(".jpg", frame)
            frame = buffer.tobytes()
            yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


@app.route("/camera")
def camera_page():
    return render_template("camera.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/")
def index():
    temperature = random.randint(20, 30)  # 生成隨機溫度值（範例：20°C 至 30°C）
    humidity = random.randint(40, 60)  # 生成隨機濕度值（範例：40% 至 60%）
    return render_template("index.html", temperature=temperature, humidity=humidity)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
