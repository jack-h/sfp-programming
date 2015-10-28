#! /usr/bin/env python
import os
import sys
import struct
import time

# usage:
# i2csetter.py input-binary-file

infile = sys.argv[1]
addr = 0x50 #int(sys.argv[2],16)
page = 0 #int(sys.argv[3],16)

offset = 128

#os.system('i2cset -y 1 0x%.2x 0x7f 0x%.2x'%(addr, page))

print 'Writing from file', infile

with open(infile, 'r') as fh:
    string = fh.read()

print 'Read %d bytes'%len(string)

vals = struct.unpack('256B', string)

for vn, v in enumerate(vals):
    if vn >= 128:
        break
    #print 'Writing val %x to location %x'%(v,vn)
    print 'calling i2cset -y 1 0x%.2x 0x%.2x 0x%.2x'%(addr, vn+offset,v)
    os.system('i2cset -y 1 0x%.2x 0x%.2x 0x%.2x'%(addr, vn+offset,v))
    time.sleep(0.05)
