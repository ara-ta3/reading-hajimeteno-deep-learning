import sys, os
sys.path.append(os.curdir + "/lib")
sys.path.append(os.curdir + "/lib/deel")
from deel import *
from deel.network import *
from deel.commands import *
import argparse


def main(argv):
    deel = Deel()
    CNN = Alexnet()
    CNN.Input(args.image)
    CNN.classify()
    ShowLabels()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", "-p", default="./lib/deel/deel.png")
    args = parser.parse_args()
    main(args)

