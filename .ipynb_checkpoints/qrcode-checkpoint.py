import qrcode
num=f"BEGIN:V\n0123\nEND:V"
img=qrcode.make(num)
img.save('num.png')