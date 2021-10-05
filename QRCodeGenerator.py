import qrcode
import qrcode.image.svg
import qrcode.image.styles.moduledrawers
import sys

def encodedString(stringList):
    if len(stringList) > 3:
        s = "WIFI:S:"+stringList[0]+";T:"+stringList[1] + \
            ";P:"+stringList[2]+";H:"+stringList[3]+";"
    else:
        s = ""
    return s

def main(argv):
    if (len(argv) < 2):
        print('Usage: arguments SSID SecurityType(WEP/WPA) Password Hidden(True/False)')
    s = encodedString(argv[1:len(argv)])
    qr = qrcode.QRCode()
    qr.add_data(s)
    #type(qr)
    img = qr.make_image(image_factory=qrcode.image.svg.SvgImage,
                        module_drawer=qrcode.image.styles.moduledrawers.RoundedModuleDrawer(radius_ratio=8))
    img.save("qrCode.svg")


if __name__ == '__main__':
    main(sys.argv)
