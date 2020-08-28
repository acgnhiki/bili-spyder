# bili-spyder

Calculating the signature of the Bilibili's heartbeat requests

**For the moment, only supported on Unix platforms with a x86-64 architecture!**

## Installation
1. install this package by pip first.

    `pip3 install bili-spyder`

2. check if the [Imported functions](https://github.com/wasmerio/python-ext-wasm#imported-functions) feature is supported or not.

    `python3 -c "from wasmer import Features; print(Features.host_functions())"` 

    if it printed out `True`, skip the steps below, otherwise follow the steps below.

3. compile a new `wasmer` by yourself. the issue https://github.com/wasmerio/python-ext-wasm/issues/215 may help you, good lucky!

    if you don't want to compile one by yourself and the Python verison you used is 3.8, consider the one I compiled.

    https://github.com/acgnhiki/python-ext-wasm/releases/download/0.4.2-beta.11/wasmer-0.4.2_beta_11-cp38-cp38-manylinux1_x86_64.whl

4. use the new one to reinstall `wasmer`.

## Usage
```python
from bili_spyder import calc_sign, calc_sign_async

data = {
    'id': '[1, 33, 1, 23058]',
    'device': '["AUTO8115983198593723", "2ddca4d0-2e72-427e-9b97-55ee70536381"]',
    'ets': 1598401991,
    'benchmark': 'seacasdgyijfhofiuxoannn',
    'time': 300,
    'ts': 1598402290937,
}

secret_rule = [2, 5, 1, 4]

sign = calc_sign(data, secret_rule)
sign = await calc_sign_async(data, secret_rule)
```

## About the wasm file
the wasm file is downloaded from https://i0.hdslb.com/bfs/live/e791556706f88d88b4846a61a583b31db007f83d.wasm and the file name is its `sha1`.

## Special Thanks
This project is inspired by and got much help from the project https://github.com/lkeme/bilibili-pcheartbeat
