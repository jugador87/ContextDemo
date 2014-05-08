#!/usr/bin/python
import processAudio
import time

if __name__ == '__main__':
    # process n samples of s seconds each, k seconds apart
    # print loudness, pitch
	"""
    n=10
    s=2
    k=3
    for i in xrange(n):
        print processAudio.sampleAudio(s)
        time.sleep(k)
	"""


	# continuously print loudness and pitch, record until silent
	processAudio.waitRecordToFile('demo.wav')


