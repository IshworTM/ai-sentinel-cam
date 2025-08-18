# 🛎️ AI-Powered Face Detection & Alert System

This project is like a smart doorman for your computer.
Whenever someone shows up in front of your webcam, it will:

-   👀 Detect their face in real time
-   📸 Take a snapshot and save it locally
-   🔔 Play an alert sound
-   📧 Optionally send you an email with the snapshot attached
-   📱 Optionally send you a desktop notification or Pushbullet alert

So basically, it watches your door (or screen) for you and notifies you
if someone's there.

------------------------------------------------------------------------

## ✨ Features

-   **Real-time Face Detection** using
    [face_recognition](https://github.com/ageitgey/face_recognition)
-   **Snapshot Saving** to your `~/Pictures/FDS_Snapshots/` directory
-   **Email Alerts** (with snapshot attached)
-   **Desktop Notifications** (via
    [Plyer](https://github.com/kivy/plyer))
-   **Push Notifications** with
    [Pushbullet](https://www.pushbullet.com/)
-   **Alert Sound** whenever a face is detected

------------------------------------------------------------------------

## 🛠️ Requirements

Make sure you've got these packages installed:

-   Python 3.10+
-   OpenCV (`cv2`)
-   `face_recognition`
-   `playsound`
-   `plyer`
-   `pushbullet.py`
-   `python-dotenv`

First setup a Virtual Environment (highly recommended):

```bash
python3 -m venv <venv_name>
source <venv_path>/bin/activate
```

Then, install the requirements with:

``` bash
pip install opencv-python face_recognition playsound plyer pushbullet.py python-dotenv
```

> ⚠️ Note: the above packages may require extra system dependencies
> (dlib, cmake). Check their docs if installation gives you errors.

------------------------------------------------------------------------

## ⚙️ Setup

1.  Clone this repo.

2.  Create a `.env` file in the project root with your email/Pushbullet
    settings:

    ``` env
    SERVER=smtp.gmail.com
    PORT=587
    EMAIL_NAME=youremail@gmail.com
    PASSWORD=your-app-password
    MAIL=recipient@gmail.com
    ACCESS_TOKEN=your_pushbullet_token
    ```

    > For Gmail, you'll need an **App Password**, not your normal login
    > password.

3.  Make sure `./sound/alert.wav` exists (replace with your own sound if
    you want).

------------------------------------------------------------------------

## 🚀 Usage

Run it using:

``` bash
cd src/ # Move into the src directory
python main.py # Run the script
```

The webcam window will open up.
Press **`q`** to quit at any time.

------------------------------------------------------------------------

## 🧑‍💻 Config

Inside the script, you can toggle these options:

``` python
send_email = True          # Send email with snapshot
send_notification = True   # Send local desktop notification
send_alert = True          # Play sound and send alerts (This needs to be True to send notifications)
push = True                # Send Pushbullet notification
```

Set them to `False` if you don't need them.

------------------------------------------------------------------------

## 📂 Snapshots

All snapshots are saved automatically to:

```bash
    ~/Pictures/FDS_Snapshots/   #/home/<user_name>/Pictures/FDS_Snapshots/
```

Filenames look like:

```bash
    fds_snapshot_2025-08-18_12:34:56.png
```

------------------------------------------------------------------------

## 🔮 Future Ideas

-   Add face recognition (to differentiate between family and
    strangers).
-   Hook into IoT devices (unlock your smart door, turn on lights,
    etc.).
-   Mobile app integration.

------------------------------------------------------------------------

## 💡 Inspired By

[Visit GitHub Profile](https://github.com/ProgrammingHero1/AI_powered_Door_Bell)

## ⚠️ Disclaimer

This project is for **personal / educational use only**. Don't rely on
it as your only home security system.

## ⚖️ License

MIT License. Do whatever you want, just don’t claim you made it from scratch if you didn’t. Be chill.
