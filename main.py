from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from PIL import Image

while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass
def encrypt(img_name):
    lst = []
    with open(img_name, 'rb') as img:
        imgdata = img.read()
        for img1 in imgdata:
            lst.append(img1)
    img.close()
    data = imgdata
    cipher = DES3.new(key, DES3.MODE_EAX)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(data)
    with open('Encrypted.jpg', 'wb') as img:
        img.write(imgdata)
    print("Encryption complete!!!!")

def decrypt():
    lst = []
    with open('Encrypted.jpg', 'rb') as img:
        imgdata = img.read()
        for img1 in imgdata:
            lst.append(img1)
    img.close()
    data = imgdata
    cipher = DES3.new(key, DES3.MODE_EAX)
    plaintext = cipher.decrypt(data)
    with open('Encrypted.jpg', 'wb') as img:
        img.write(imgdata)
    print("Decryption complete!!!")
def main():
    image_name = input('Enter the name of the image to be Encrypted')
    encrypt(image_name)
if __name__=='__main__':
    main()