#!/usr/bin/python
import struct

fw = open("compressed.h", "w+b")
fw.write(b"#include <stdint.h>\n")
totlen=0
for k in range(0,16):
    fr = open("compressed/output_"+str(k)+".rle", "rb")
    dat = fr.read()
    totlen+=len(dat)
    fw.write(format("const uint8_t compressed_frame_"+str(k)+"[] = {").encode())

    for i in range(0, len(dat)):
        little = struct.pack("<I", dat[i])
        out = struct.unpack(">I", little)
        fw.write(f"{dat[i]:#x},".encode()) #remember: byteorder should be big
    fw.seek(-1,2)
    fw.write(b"};\n")


    fr.close()
print(totlen)
fw.close()
