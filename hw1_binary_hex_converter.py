# -*- coding: utf-8 -*-
"""基礎資料結構與演算法作業1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yhwtQELsuNklg79elHv9YX400V2s-s1S
"""

num = int(input())
binum = ""
hexnum = ""
hexToBinary= {'0000':'0', '0001':'1', '0010':'2','0011':'3', '0100': '4', '0101': '5', '0110':'6', '0111': '6', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
i = 7
while i>=0:
  if num >= 2**i:
    num = num - 2**i
    binum = binum + "1"
    i = i - 1
  else:
    binum = binum + "0"
    i = i - 1
hexnum = hexToBinary[binum[0:4]]
hexnum = hexnum + hexToBinary[binum[4:8]]

print(binum,hexnum)