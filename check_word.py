#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # this file was tetched from
    # https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    try:
        word = sys.argv[1]
    except IndexError:
        print "This script expects one argument."
        sys.exit()

    tlds = map(lambda x: x.strip(), 
               open('./tlds-alpha-by-domain.txt', 'r').readlines())
    possibilities = filter(lambda x: word[-len(x):].upper() == x, tlds)
    print possibilities
