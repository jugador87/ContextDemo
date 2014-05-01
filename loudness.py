#!/usr/bin/python
import numpy
import time
import analyse
import pyaudio
import psutil
import thread

timeout=True

def timer(numSeconds, dummy=True):
    global timeout
    time.sleep(numSeconds)
    timeout = True

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

# Open input stream, 16-bit mono at 44100 Hz
# CSC: device 0 is built in mike?
# expected loudness output: -1dB for very loud; downto -36dB "typical silence"
chunk=1024
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 48000,
    input_device_index = 0,
    input = True)

while True:
	# Read raw microphone data
	rawsamps = stream.read(chunk)
	# Convert raw data to NumPy array
	samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
	# Show the volume and pitch
	print analyse.loudness(samps), analyse.musical_detect_pitch(samps)
