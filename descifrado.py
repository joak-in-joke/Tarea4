import os
import time

time_start = time.time()

os.system('hashcat -m 0 -a 0 -o cracked-archivo1 archivo_1 diccionario_1.dict diccionario_2.dict')

print( "SEC: " + str(time.time()-time_start))

os.system('hashcat -m 10 -a 0 -o cracked-archivo2 archivo_2 diccionario_1.dict diccionario_2.dict')

print( "SEC: " + str(time.time()-time_start))

os.system('hashcat -m 10 -a 0 -o cracked-archivo3 archivo_3 diccionario_1.dict diccionario_2.dict')

print( "SEC: " + str(time.time()-time_start))

os.system('hashcat -m 1000 -a 0 -o cracked-archivo4 archivo_4 diccionario_1.dict diccionario_2.dict')

print( "SEC: " + str(time.time()-time_start))

os.system('hashcat -m 1800 -a 0 -o cracked-archivo5 archivo_5 diccionario_1.dict diccionario_2.dict')

print( "SEC: " + str(time.time()-time_start))