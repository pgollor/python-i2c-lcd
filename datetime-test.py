#! /usr/bin/python

from lcddriver import lcd
from time import sleep
from datetime import datetime

my_lcd = lcd()

my_lcd.display_string("LCD", 1)
my_lcd.display_string("Hello World", 2)

while (True):
	sleep(1)

	my_lcd.clear()

	dateString = datetime.now().strftime('%Y-%m-%d')
	timeString = datetime.now().strftime('%H:%M:%S')
	my_lcd.display_string(dateString, 1)
	my_lcd.display_string(timeString, 2)
# end while
