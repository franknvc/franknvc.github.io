from flask import Flask, Response
from flask import render_template
import threading
import argparse
import time
import imutils
from imutils.video import VideoStream
import cv2

output_frame = None
lock = threading.Lock()

app = Flask(__name__)

vs = VideoStream(src=0).start()
time.sleep(2.0)


@app.route("/")
def index():
    return render_template("index.html")


def capture(frame_count):
    global vs, output_frame, lock

    while True:
        frame = vs.read()
        frame = imutils.resize(frame, width=400)
        with lock:
            output_frame = frame.copy()


def generate():
    global output_frame, lock

    while True:
        with lock:
            if output_frame is None:
                continue

            (flag, encoded_image) = cv2.imencode(".jpg", output_frame)

            if not flag:
                continue

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encoded_image) + b'\r\n')


@app.route("/video_feed")
def video_feed():
    return Response(generate(),
                    mimetype="multipart/x-mixed/replace boundary=frame")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, required=True, help="ip address of the device")
    parser.add_argument("-o", "--port", type=int, required=True, help="ephemeral port number of the server")
    args = vars(parser.parse_args())

    t = threading.Thread(target=capture, args=(
        args["frame_count"],))

    t.daemon = True
    t.start()

    app.run(host=args["ip"], port=args["port"], debug=True, threaded=True, use_reloader=False)

vs.stop()