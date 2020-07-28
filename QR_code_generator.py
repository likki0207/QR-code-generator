import qrcode
import cv2

qrcode=qrcode.QRCode(
    version = 1,  # It will take an integer from 1 to 40 to control the size of the QR code. The smaller the number, the smaller the QR code size is going to be
    error_correction = qrcode.constants.ERROR_CORRECT_M,   # ERROR_CORRECT_M is the default, it means that about 15% or lesser errors can be propagated
    box_size=15,   # Size of  QR code
    border=5       # Border for the QR code
    )



data=input('Enter the link of the site for which you want the QR code...')   # Enter the link of the site
qrcode.add_data(data) 
qrcode.make(fit=True)
image=qrcode.make_image(fill='black',back_color='white')
image.save('qr_code.png')