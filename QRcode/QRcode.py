import qrcode as qr
img= qr.make("https://disneyworld.disney.go.com/")
img.save("QRcode.png")