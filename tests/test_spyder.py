#!/usr/bin/env python3
import unittest
import asyncio

from src.bili_spyder import calc_sign, calc_sign_async

data = {
    'id': '[1, 33, 1, 23058]',
    'device': '["AUTO8115983198593723", "2ddca4d0-2e72-427e-9b97-55ee70536381"]',
    'ets': 1598401991,
    'benchmark': 'seacasdgyijfhofiuxoannn',
    'time': 300,
    'ts': 1598402290937,
}

secret_rule = [2, 5, 1, 4]
correct_sign = '520ee60aa0e716b2e2d25ded7e34aafad103578d7bdb80cfa605ab3e8080c9884a2adee618cf6671d75dbe3227c4624e17e5f33e70c8de20457181040ce8569c'

class SpyderTestCase(unittest.TestCase):
    def test_calc_sign(self):
        sign = calc_sign(data, secret_rule)
        self.assertEqual(sign, correct_sign)

    def test_calc_sign_async(self):
        loop = asyncio.get_event_loop()
        sign = loop.run_until_complete(calc_sign_async(data, secret_rule))
        self.assertEqual(sign, correct_sign)

if __name__ == '__main__':
    unittest.main()
