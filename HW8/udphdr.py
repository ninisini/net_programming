import socket
import struct
import binascii

class Udphdr:
    def __init__(self, saddr, daddr, tot_len, check):
        self.saddr = saddr
        self.daddr = daddr
        self.tot_len = tot_len
        self.check = check

    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack('!HH', self.saddr, self.daddr)
        packed += struct.pack('!HH', self.tot_len, self.check)
        return packed
    
def unpack_Udphdr(buffer):
        unpacked = struct.unpack('!HHHH', buffer[:8])
        return unpacked

def getSrcPort(unpack_Udphdr):
        return (unpack_Udphdr[0])

def getDstPort(unpack_Udphdr):
        return (unpack_Udphdr[1])

def getLength(unpack_Udphdr):
        return (unpack_Udphdr[2])

def getChecksum(unpack_Udphdr):
        return (unpack_Udphdr[3])

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_Udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_Udphdr))

unpack_Udphdr = unpack_Udphdr(packed_Udphdr)
print(unpack_Udphdr)
print('Source Port: {} Destination Port: {} Length: {} Checksum: {}'\
    .format(getSrcPort(unpack_Udphdr), getDstPort(unpack_Udphdr), getLength(unpack_Udphdr), getChecksum(unpack_Udphdr)))