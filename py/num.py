import pandas as pd
import numpy as np 

ten_tap_tin = 'customer.csv.txt'
with open(ten_tap_tin, 'r', encoding='utf-8') as file:
    test = file.read()
    print(test)