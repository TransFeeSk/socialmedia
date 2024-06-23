import qrcode

# URL you want to encode
url = "https://transfeesk.github.io/socialmedia"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save it to a file
img.save("qr_code.png")

print("QR Code generated successfully.")
