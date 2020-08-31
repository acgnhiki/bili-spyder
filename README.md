# bili-spyder

Calculating the signature of the Bilibili's heartbeat requests

## Installation

`pip install bili-spyder`

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

See also: <https://github.com/acgnhiki/bili-spyder-example>

## About the wasm file

the wasm file is downloaded from <https://i0.hdslb.com/bfs/live/e791556706f88d88b4846a61a583b31db007f83d.wasm> and the file name is its `sha1`.

## Special Thanks

This project is inspired by and got much help from the project <https://github.com/lkeme/bilibili-pcheartbeat>
