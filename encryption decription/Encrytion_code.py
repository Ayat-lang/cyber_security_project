
#function for the encryption key:
def Encryption( filename, key):
    file = open( filename, "rb")
    data = file.read()
    file.close()

    byte_array = bytearray(data)
    for index, value in enumerate(byte_array):
        byte_array[index] = key ^ value

    file = open("Encryption-" + filename, "wb")
    file.write(byte_array)
    file.close()


key = int(input("Enter the key between 1 to 255 : "))
filename = input("Enter the file name : ")
Encryption( filename, key)