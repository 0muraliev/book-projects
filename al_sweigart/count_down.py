"""Простой сценарий обратного отсчета."""

import subprocess
import time

time_left = 60
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left -= 1

# Воспроизведение звукового файла по завершении обратного отсчета.
subprocess.Popen(['aplay', 'alarm.wav'])
