#!/bin/python3

import pyqrcode
import png
from pyqrcode import QRCode

def qrcode():

	qrcode = "https://www.instagram.com/g0dmax55/"

	qr = pyqrcode.create(qrcode)

	qr.png('myqr.png', scale = 8)

qrcode()
