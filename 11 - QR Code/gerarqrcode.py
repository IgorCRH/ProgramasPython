import qrcode

linkperfil = "https://twitter.com/IgorGeoPol"

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(linkperfil)
qr.make(fit=True)
imagemqr = qr.make_image(fill_color="green", back_color="white")
imagemqr.save("qrcodeperfiltwitter.png")
