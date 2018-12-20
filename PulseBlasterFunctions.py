import spinapi as sp

ch1 = 0b000000000000000000000001
ch2 = 0b000000000000000000000010
ch3 = 0b000000000000000000000100
ch4 = 0b000000000000000000001000
ch5 = 0b000000000000000000010000
ch6 = 0b000000000000000000100000
ch7 = 0b000000000000000001000000
ch8 = 0b000000000000000010000000
all_channels = 0b111111111111111111111111

def _init():
	sp.pb_set_debug(1)
	if sp.pb_init() != 0:
		print("Error initializing board: {}".format(sp.pb_get_error()))
		exit(-1)
	sp.pb_core_clock(500)
	
	return 0

def start():
	sp.pb_start()
	return None

def stop():
	code = sp.pb_stop()
	return code

def close():
	code = sp.pb_close()
	return code

def dc(*channels):
	_ch = 0
	for i in channels:
		_ch += _ch
	_init()
	sp.pb_start_programming(sp.PULSE_PROGRAM)
	sp.pb_inst_pbonly64(_ch, sp.Inst.STOP, 0, 1*sp.us)
	sp.pb_stop_programming()
	sp.pb_start()
	code = sp.pb_close()

	return code

def ple_pulse_sequence(repeats,
	init_time = 3*sp.us,
	delay_time = 2*sp.us,
	read_time = 10*sp.us,
	green_chan = ch1,
	red_chan = ch2,
	count_chan = ch3):

	_init()
	sp.pb_start_programming()
	start = sp.pb_inst_pbonly(0x0, sp.Inst.LOOP, repeats, delay_time)
	init = sp.pb_inst_pbonly(green_chan, sp.Inst.CONTINUE, 0, init_time)
	wait = sp.pb_inst_pbonly(0x0, sp.Inst.CONTINUE, 0, delay_time)
	read = sp.pb_inst_pbonly(red_chan + count_chan, sp.Inst.END_LOOP, start, read_time)
	finish = sp.pb_inst_pbonly(0x0, sp.Inst.STOP, 0, 1*sp.us)
	sp.pb_stop_programming()
	sp.pb_start()
	code = sp.pb_close()

	return code


