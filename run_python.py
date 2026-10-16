import os
import runpy
import subprocess
from path_finder import current_dir


def run(filename):
    """
    फ़ाइल को उसी प्रोसेस में चलाएगा, उसके खत्म होने का पूरा इंतज़ार करेगा,
    और फिर आगे बढ़ेगा (बिना subprocess के 2 सेकंड का समय गंवाए)।
    """
    file_path = os.path.join(current_dir, filename)
    runpy.run_path(file_path, run_name="__main__")


def run_all_files(file_names):
    """
    सभी फ़ाइलों को बैकग्राउंड में शुरू करके तुरंत आगे बढ़ जाता है।
    """
    for file in file_names:
        full_path = os.path.join(current_dir, file)
        subprocess.Popen(["python", full_path])


def run_all(file_name):
    """
    एक फ़ाइल को बैकग्राउंड में शुरू करके तुरंत आगे बढ़ जाता है।
    """
    full_path = os.path.join(current_dir, file_name)
    subprocess.Popen(["python", full_path])