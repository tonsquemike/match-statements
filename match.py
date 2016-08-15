#!/usr/bin/python
# coding=utf-8
__author__ = 'Miguel Ángel García Calderón - tonsquemike@outlook.com'
import re
import sys, getopt

# Store input and output file names
ifile=''
ofile=''

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
 
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    else:
        print("Usage: %s -i input -o output" % sys.argv[0])
 
# Display input and output file name passed as the args
print ("Input file : %s and output file: %s" % (ifile,ofile) )

with open(ifile, 'r') as myfile:
    data=myfile.read()
print data

# Program Start
p = re.compile(ur'((?:(?:if|while|for)))\s*\(.*?\)\s*({(?:{[^{}]*}|.)*?})', re.DOTALL)
match = p.findall(data)
print match