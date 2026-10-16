import os
import signal
import subprocess
from path_finder import path

def start_audio():
    audio_file = f"{path}final.mp3"
    pid_file = f"{path}audio_player.pid"

    # Agar koi purana process chal raha ho toh silently band karein
    if os.path.exists(pid_file):
        try:
            with open(pid_file, "r") as f:
                content = f.read().strip()
                if content:
                    os.kill(int(content), signal.SIGTERM)
        except (ProcessLookupError, ValueError):
            pass

    # --loop=inf se audio non-stop bajta rahega jab tak terminate na kiya jaye
    process = subprocess.Popen(
        ["mpv", "--no-video", "--loop=inf", audio_file],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    # PID ko file me overwrite karein
    with open(pid_file, "w") as f:
        f.write(str(process.pid))


def end_audio():
    pid_file = f"{path}audio_player.pid"

    if os.path.exists(pid_file):
        try:
            with open(pid_file, "r") as f:
                content = f.read().strip()
                if content:
                    os.kill(int(content), signal.SIGTERM)
        except (ProcessLookupError, ValueError):
            pass

        # File ko delete karne ke bajaye blank (empty) karein
        with open(pid_file, "w") as f:
            f.write("")



def play_won():
    audio_file = f"{path}won.mp3"
    
    # Background me chalega, aage ka code nahi rukega, ek baar play ho kar khud exit ho jayega
    subprocess.Popen(
        ["mpv", "--no-video", audio_file],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
def fass():
    audio_file = f"{path}fass.mp3"
    
    # Background me chalega, aage ka code nahi rukega, ek baar play ho kar khud exit ho jayega
    subprocess.Popen(
        ["mpv", "--no-video", audio_file],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def holidayss():
    audio_file = f"{path}holiday.mp3"
    
    # Background me chalega, aage ka code nahi rukega, ek baar play ho kar khud exit ho jayega
    subprocess.Popen(
        ["mpv", "--no-video", audio_file],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

