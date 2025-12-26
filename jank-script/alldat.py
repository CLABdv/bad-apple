#!/usr/bin/python
import struct
#width = 320
#height = 240
#i can therefore make each frame an array of 240 * 10 uint32_t's
#nframes = 5840 #THIS IS TOTAL

size = struct.calcsize("<I")
for i in range(0,16):
    fw = open(f"alldat_{i}.dat", "wb")
    for k in range(1,401,8):
        filename = "output"+"_"+str(k+i*400).zfill(4)
        fr = open("frames/"+filename+".pbm", "rb")
        fr.read(11) #header
        while chunk := fr.read(size):
            value = struct.unpack("<I", chunk)[0]
            fixed_chunk = struct.pack(">I", value)
            fw.write(fixed_chunk)
        fr.close()
    fw.close()
