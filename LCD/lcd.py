import lcddriver
from time import *


lcd = lcddriver.lcd()			#Declare a lcddriver object

lcd.lcd_clear()				#Clear the LCD display



lcd.lcd_display_string("    Hello, World !",4)
lcd.lcd_display_string("      HERO bot",3)
lcd.lcd_display_string("       TEAM 5",1)

