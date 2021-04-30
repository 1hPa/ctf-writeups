### セキュリティ機構
```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      PIE enabled
```

### TL;DR
単純なBOF後に関数を呼び出す。

### 解法
デバッグすると、入力のオフセットが72であることがわかる。  
また、`ReadFlag`関数と`PrintFlaga`関数があるので、BOF後に渡すと
関数が実行されて、`Flag`が出力される。
