#!_*_coding:utf-8_*_


import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

from s14day5.home_work.atm.core import main

if __name__ == '__main__':
    main.run()