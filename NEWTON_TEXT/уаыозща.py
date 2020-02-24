#!/usr/bin/python
# -*- coding: utf-8 -*-
from tqdm import tqdm
for i in tqdm(range(int(1e6)), ncols=100, desc='Закгрузка системы'):
    pass

import time

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    time.sleep(0.25)
    text = text + char

for i in range(100):
    time.sleep(0.01)

pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    time.sleep(1)
    pbar.set_description("Processing %s" % char)
