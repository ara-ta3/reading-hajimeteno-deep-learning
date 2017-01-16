import sys, os
sys.path.append(os.curdir + "/lib")
sys.path.append(os.curdir + "/lib/deel")
from deel import *
from deel.network import *
from deel.commands import *

deel = Deel()
CNN = Alexnet()
CNN.Input("./lib/deel/deel.png")
CNN.classify()
ShowLabels()
