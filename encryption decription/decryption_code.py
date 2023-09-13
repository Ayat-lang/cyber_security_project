

def Decryption( filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    byte_array = bytearray(data)
    for index, value in enumerate(byte_array):
        byte_array[index] = value ^ key
    
    file = open("Extract_Data" + filename, "wb")
    file.write(byte_array)
    file.close()
    


key = int(input("Enter the Encryption key For extract the data : "))
filename = input("Enter the Encrypted file name : ")
Decryption( filename, key)
