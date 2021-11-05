import qrcode

qr = qrcode.QRCode(version=1 , error_correction = qrcode.constants.ERROR_CORRECT_L, box_size=20,border=2)


add = input("Enter link or anything: ")
qr.add_data(add)
qr.make(fit=True)

img =  qr.make_image(fill_color='black', back_color='white')

img.save("Advanced.png")