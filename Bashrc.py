#!/usr/bin/python3.4

import sys
import os


class Bashrc:
    """it's a code for Linux and Unix"""

    def __init__(self):
        """position $HOME/.bashrc and order for write in file"""
        self.posFile = os.environ["HOME"] + "/.bashrc"
        self.order = {"PATH": self.PATH,
                      "ALIAS": self.ALIAS}

    def PATH(self):
        return "PATH=" + sys.argv[2] + ":$PATH \nexport PATH"

    def ALIAS(self):
        return "alias " + sys.argv[2] + "='" + sys.argv[3] + "'"

    def add(self):
        with open(self.posFile, "a") as file:
            file = file.write("{0}\n".format(self.order[sys.argv[1]]()))

    def exeCMD():
        try:
            x = Bashrc()
            x.add()
        except IndexError:
            print ("Bashrc")
            print ("argv 1 = ALIAS,PATH")
            print ("argv 2 = your path the export PATH or the name for alias")
            print ("argv 3 : it's the path for alias")
if __name__ == "__main__":
    Bashrc.exeCMD()
    
