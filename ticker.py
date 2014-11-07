__author__ = 'aharvey'
import serial
import string
import ystockquote

INIT = chr(170) + chr(170)+ chr(170)+chr(170)+chr(170)+chr(187)+chr(146)
CLEAR = chr(140) + chr(140)

def cvtStr(msg):
    msg = string.replace(msg," ", "%20")
    msg = string.replace(msg, ":", " ")
    msg = string.replace(msg, "%20", ":")
    msg = string.replace(msg, "<LEFT>", chr(129))
    msg = string.replace(msg, "<RIGHT>", chr(130))
    msg = string.replace(msg, "<UP>", chr(131))
    msg = string.replace(msg, "<DOWN>", chr(132))
    msg = string.replace(msg, "<JUMP>", chr(133))
    msg = string.replace(msg, "<OPEN>", chr(134))
    msg = string.replace(msg, "<CLOSE>", chr(135))
    msg = string.replace(msg, "<FLASH>", chr(136))
    msg = string.replace(msg, "<FLASHGO>", chr(137))
    msg = string.replace(msg, "<SPELL>", chr(138))
    msg = string.replace(msg, "<FAT>", chr(139))
    msg = string.replace(msg, "<CLEAR>", chr(140))
    msg = string.replace(msg, "<SPEED>", chr(141))
    msg = string.replace(msg, "<RANDOM>", chr(142))
    msg = string.replace(msg, "<PAUSE>", chr(143))
    return msg

ser = serial.Serial(0, 2400, timeout=1)
ser.write(INIT)

ser.write(CLEAR)
ser.write(cvtStr("FTNT %s %0.2f" % ()))
ser.write(chr(128))

ser.close()

