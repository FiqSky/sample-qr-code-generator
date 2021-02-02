import pyqrcode
import os
import shutil

title = input("Type name QR Code: ")
text = input("Type your text to generate QR Code: ")

file_name_svg = title + ".svg"
file_name_png = title + ".png"

url = pyqrcode.create(text)

url.svg(file_name_svg, scale=8)
url.png(file_name_png, scale=10)

os.mkdir(fr"C:\work\Python\QRCodeGenerator\{title}")

shutil.move(f"{file_name_svg}", fr"C:\work\Python\QRCodeGenerator\{title}")
shutil.move(f"{file_name_png}", fr"C:\work\Python\QRCodeGenerator\{title}")
