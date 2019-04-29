#!/usr/bin/env python

class Minterm:
    def __init__(self, row, variables):
        self.row = row
        self.variables = variables

    def _convert_row_binary(self):
        '''Return a binary representation of the row number'''
        binary = "{0:b}".format(self.row)
        if len(binary) < self.variables:
            for i in range(self.variables - len(binary)):
                binary = "0" + binary
        return binary

    def get_table_format(self):
        res = ""
        binary = self._convert_row_binary()
        for i in range(len(binary)):
            if binary[i] == "0":
                res = res + "~"
            res = res + chr(65 + i)
            if i != (len(binary) - 1):
                res = res + "*"
        return res

    def __str__(self):
        return self.get_table_format()

    __repr__ = __str__ 
