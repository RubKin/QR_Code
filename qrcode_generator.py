import qrcode 

feats = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    box_size=40, 
    border=3
    )
user_input = input("Enter your Hyperlink...   ")

feats.add_data(user_input)

feats.make(fit=True)

img = feats.make_image(
    fill_color="black", 
    back_color="white"
    )

img.save("./qrcodes/sistema_qr.png")


#https://www.youtube.com/watch?v=_x3EjByP5Mg

#https://pypi.org/project/qrcode/
#check SVGs
#style the images

