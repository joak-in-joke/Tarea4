import os
import time
import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

time_start = time.time()

file1 = open('cracked-archivo5', 'r') 
Lines = file1.readlines() 

file2 = open('new_archivo_5', 'w') 

for line in Lines: 
    salt = binascii.unhexlify('df1f2d3f4d77ac66e9c5a6c3d8f921b6')
    passwd = str(line).encode("utf8")
    key = pbkdf2_hmac("sha256", passwd, salt ,90000, 32)
    print("Derived key:", binascii.hexlify(key))
    file2.writelines(binascii.hexlify(key).decode('ascii')+"\n")


file2.close() 

print( "SEC: " + str(time.time()-time_start))