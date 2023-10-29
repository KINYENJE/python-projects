import pyqrcode
import os , shutil
import time

# Path: qrCode/qrCode.py
title = input("Enter the title of the QR code: ")
text = input("Enter the text of the QR code: ")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create("https://rafasgit.github.io/mzitosupercuts/")


url.svg(file_name_svg, scale=8)
url.png(file_name_png, scale=6)

# os.mkdir(fr'C:\Users\ADMIN\Desktop\{title}')

# shutil.move(fr'C:\Users\ADMIN\Desktop\{file_name_svg}', fr'C:\Users\ADMIN\Desktop')
