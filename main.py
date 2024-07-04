import qrcode
import image

qrNesnesi=qrcode.QRCode(version=15,
box_size=10,
border=5)

veri="Mustafa Emir Ata"
qrNesnesi.add_data(veri)
qrNesnesi.make(fit=True)

img=qrNesnesi.make_image(fill="black",back_color="white")
img.save("qr.png")