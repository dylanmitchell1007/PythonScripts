import os

class object(object):
    def __init__(self, string):
        self.string = string
def Main():
    test = object("A, B, D, E, F")

    print test.string
    os.system("pause")

Main()
