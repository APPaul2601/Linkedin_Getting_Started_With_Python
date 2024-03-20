# It creates a bytes object that is 4 bytes long
print(bytes(4))

# 2 hexadecimal is 256 possibilities, which is the same as 2 to the power of eight (eight bits) and there are
# 8 bits to a byte

smile = bytes('😁', 'utf-8')  # you need to tell python what format it is, in this case emoji is a utf-8
print(smile)

smile_bytes = smile.decode('utf-8')
print(smile_bytes)

# Bytes are immutable

smile_1 = bytearray('😁', 'utf-8')
print(smile_1)

smile_1[3] = int('85', 16)

print(smile_1.decode('utf-8'))
