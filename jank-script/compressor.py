#!/usr/bin/python
import numpy as np
k=1000
#basename = f"output_{k}"
fw = open("output.rle", "w+b")
filename = "output_"+str(k).zfill(4)
fr = open("frames/"+filename+".pbm", "rb")
#fr = open(f"alldat_{k}.dat", "rb")
header = fr.read(11)

dat = fr.read()
#print(dat)

def compress_data(bytes):
    l = len(bytes)
    i = 0
    prev_bit = (bytes[0]&0x80).bit_count()
    mask = 0x80
    compressed_list = []
    while(i < l):
        counter = 0
        while((bytes[i] & mask).bit_count() == prev_bit):
            if counter == 0x7f:
                compressed_list.append(counter | prev_bit << 7)
                #print(f"{counter} pixels of {prev_bit}")
                counter = 0
            if mask == 0x01:
                i+=1
                if(i == l):
                    counter+=1
                    compressed_list.append(counter | prev_bit << 7)
                    #print(f"{counter} pixels of {prev_bit}")
                    return compressed_list
                mask = 0x80
            else:
                mask >>= 1
            counter += 1
        compressed_list.append(counter | prev_bit << 7)
        #print(f"{counter} pixels of {prev_bit}")
        prev_bit = (bytes[i] & mask).bit_count()
    return compressed_list

l=compress_data(dat)
fw.write(bytes(l))
fw.close()


def image_from_compressed(bytes):
    fw = open("uncompressed.ppm", "wb")
    fw.write(header)
    array = np.zeros(320*240, dtype=np.uint8)
    i = 0
    prev_ind = 0
    for i in range(0,len(bytes)):
        val = bool(bytes[i]&0x80)
        count = bytes[i]&0x7f
        array[prev_ind:prev_ind+count] = val
        prev_ind += count
    byte_values = np.packbits(array)
    fw.write(bytearray(byte_values))
    fw.close()

image_from_compressed(bytes(l))
