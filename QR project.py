## Import QR code
import qrcode

# Creating a QR code of (youtube - Perfect - Ed Sheeran)
data = "https://www.youtube.com/watch?v=2Vv-BfVoq4g"

img = qrcode.make(data)

img.save("C:/Users/angel/Desktop/DATA SCIENCE/Learning projects/Images for qr code/myqrcode.png")

