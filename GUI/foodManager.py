import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from 번호표시스템.manager import *
from 번호표시스템.twilioTest import *

gama = Manager("가마")
noodle = Manager("누들송(면)")
inter = Manager("인터쉐프")
daily = Manager("데일리밥")

gama.setWaitingTime(2)
noodle.setWaitingTime(2)
inter.setWaitingTime(2)
daily.setWaitingTime(2)

def buttonClicked2(self):
    pass