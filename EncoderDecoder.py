from PIL import Image
import binascii
import optparse

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
    return tuple(int(hexcode[i:i+2], 16) for i in range(1, len(hexcode), 2))
def string2bin(message):
    if message:
        # Encode the string into bytes
        message_bytes = message.encode('utf-8')
        # Use binascii.hexlify() with the bytes-like object
        hex_representation = binascii.hexlify(message_bytes).decode('utf-8')
        # Convert hex to binary with leading zeros preserved
        binary = ''.join(format(int(hex_char, 16), '04b') for hex_char in hex_representation)
        return binary
    else:
        return ''

def bin2string(binary):
    message = binascii.unhexlify('%x' % (int('0b' + binary, 2)))
    return message
def encode(hexcode, digit):
    if hexcode[-1] in ('0', '1', '2', '3', '4', '5'):
        hexcode = hexcode[:-1] + digit
        return hexcode
    else:
        return None
def decode(hexcode):
    if hexcode[-1] in ('0', '1'):
        return hexcode[-1]
    else:
        return None
def hide(filename, message):
    img = Image.open(filename)
    binary = string2bin(message) + '1111111111111110'
    if img.mode in('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()

        newData = []
        digit = 0
        temp = ''
        for item in datas:
            if (digit < len(binary)):
                newpix = encode(rgb2hex(item[0], item[1], item[2]), binary[digit])
                if newpix == None:
                    newData.append(item)
                else:
                    r, g, b = hex2rgb(newpix)
                    newData.append((r, g, b, 255))
                    digit += 1
            else:
                newData.append(item)
        img.putdata(newData)    
        img.save(filename, "PNG")
        return "Completed!"
    return "Incorrect Image Mode, Couldn't Hide"
def retr(filename):
    img = Image.open(filename)
    binary = ''
    if img.mode in ('RGBA'):
        img = img.convert('RGBA')
        datas = img.getdata()
        for item in datas:
            digit = decode(rgb2hex(item[0], item[1], item[2]))
            if digit == None:
                pass
            else:
                binary = binary + digit
                if (binary[-16:] == '1111111111111110'):
                    print("Success")
                    return bin2string(binary[:-16])
        return bin2string(binary)
    return "Incorrect Image Mode, Couldn't Retrieve"
def Main():
    parser = optparse.OptionParser('usage %prog' + '-e/-d <target file>')
    parser.add_option('-e', dest='hide', type='string', help='target picture path to hide text')
    parser.add_option('-d', dest='retr', type='string', help='target picture path to retrieve text')
    (options, args) = parser.parse_args()
    if (options.hide != None):
        text = "This is the message hidden. Congratulations on finding it!"
        print (hide(options.hide, text))
    elif (options.retr != None):
        print (retr(options.retr))
    else:
        print (parser.usage)
        exit(0)
if __name__ == '__main__':
    Main()
    