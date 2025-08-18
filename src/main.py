import os
from threading import Thread
from cv2 import VideoCapture, imshow, waitKey, imwrite, imencode, typing
from playsound import playsound
from face_recognition import face_locations
from smtplib import SMTP
from socket import gaierror
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
from plyer import notification
from datetime import datetime
from pushbullet import Pushbullet


def alert_user(
    image_path: str,
    image_frame: bytes | bytearray,
    send_email: bool = False,
    send_notification: bool = False,
    push: bool = False,
):
    Thread(target=playsound, args=("./sound/alert.wav",), name="Ding Dong").start()
    title = "Face Detected 👀"
    message = f"Alert!! Someone is at the door."
    if send_email:
        image_data = convert_frame_to_bytes(image_frame)
        res, msg = email_user(title=title, message=message, image_data=image_data)
        notification.notify(
            title="Sending email.." if res else "Cannot send email..",
            message=msg,
            timeout=8,
        )
    if send_notification:
        message += f"\nSnapshot saved to:\n{image_path}"
        notify_user(title, message, push)


def convert_frame_to_bytes(frame: typing.MatLike) -> bytes:
    _, buffer = imencode(".jpg", frame)
    return buffer.tobytes()


def notify_user(title, message, push=False) -> dict:
    res = {}
    if not push:
        notification.notify(
            title=title,
            message=message,
            timeout=8,
        )
        res["sent"] = True
        res["title"] = title
        res["body"] = message
    else:
        pb = Pushbullet(os.getenv("ACCESS_TOKEN"))
        res = pb.push_note(title=title, body=message)
    return res


def email_user(title: str, message: str, image_data: bytes) -> tuple[bool, str]:
    server = os.getenv("SERVER")
    port = int(os.getenv("PORT"))
    server_mail = os.getenv("EMAIL_NAME")
    server_password = os.getenv("PASSWORD")

    data = MIMEMultipart()
    data["From"] = server_mail
    data["To"] = os.getenv("MAIL")
    data["Subject"] = title

    body = f"Information: {message}"
    data.attach(MIMEText(body, "plain"))
    data.attach(MIMEImage(image_data))
    try:
        _server = SMTP(server, port)
        _server.starttls()
        _server.login(server_mail, server_password)
        _server.send_message(data)
        _server.quit()
        return True, "Email sent successfully!"
    except gaierror:
        return (
            False,
            "Cannot send email, please check your internet connection and try again.",
        )
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"


def main(
    send_alert: bool = False,
    send_email: bool = False,
    send_notification: bool = False,
    push: bool = False,
):
    capture = VideoCapture(0)
    snapshot_dir = os.path.expanduser("~/Pictures/FDS_Snapshots")
    os.makedirs(snapshot_dir, exist_ok=True)
    alert_sent = False
    while 1:
        _, frame = capture.read()
        coords = face_locations(frame)
        if coords and send_alert and not alert_sent:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            image_path = os.path.join(snapshot_dir, f"fds_snapshot_{timestamp}.png")
            imwrite(image_path, frame)
            alert_user(
                image_path=image_path,
                image_frame=frame,
                send_email=send_email,
                send_notification=send_notification,
                push=push,
            )
            alert_sent = True
        elif not coords and alert_sent:
            alert_sent = False

        imshow("Face Detection and Alert System", frame)
        if waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    send_email = True
    send_notification = True
    send_alert = True
    push = True
    load_dotenv("./.env")
    main(send_email, send_notification, send_alert, push)
