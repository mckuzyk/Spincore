from spinapi import *

class PulseBlaster(object):

	def __init__(self):
		self.ch1 = 0b000000000000000000000001
		self.ch2 = 0b000000000000000000000010
		self.ch3 = 0b000000000000000000000100
		self.ch4 = 0b000000000000000000001000
		self.ch5 = 0b000000000000000000010000
		self.ch6 = 0b000000000000000000100000
		self.ch7 = 0b000000000000000001000000
		self.ch8 = 0b000000000000000010000000
		self.all_channels = 0b111111111111111111111111

	def _init(self):

		pb_set_debug(1)
		if pb_init() != 0:
			print("Error initializing board: {}".format(pb_get_error()))
			exit(-1)

		pb_core_clock(500)

	def start(self):
		pb_start()

	def stop(self):
		pb_stop()

	def close(self):
		pb_close()


