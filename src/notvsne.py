#! /usr/bin/python

import dis

def caseNot():
    if not not 0: return None

def caseNe():
    if 0 != 1: return None

def caseFalse():
    if False: return None

print "case not"
dis.dis(caseNot)
print "case !="
dis.dis(caseNe)
print "case false"
dis.dis(caseFalse)
