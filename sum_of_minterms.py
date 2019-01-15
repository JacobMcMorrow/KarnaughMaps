#!/usr/bin/env python

from minterm import Minterm

class SumOfMinterms:
    def __init__(self, minterms):
        self.minterms = minterms

    def __str__(self):
        res = ' + '.join(str(minterm) for minterm in minterms)
        return res

    __repr__ = __str__
