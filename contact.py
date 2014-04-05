#!/usr/bin/python

import getopt, sys

'''
Thanks for your interest! I look forward to getting to know you
'''
def main():
    experience = {'Java': 8.0, 'Scala': 0.5, 'Oracle': 7.5, 'Python': 2.0}
    opts, args = getopt.getopt(sys.argv[1:], "ncalm", 
        ["name", "contact", "about", "links", "misc"])
    for opt, arg in opts:
        if opt in ("-n", "--name"):
            print "Andrea Fey"
        elif opt in ("-c", "--contact"):
            print "andrea.fey@gmail.com  |  828.243.7502"
        elif opt in ("-a", "--about"):
            print experience
        elif opt in ("-l", "--links"):
            print "github.com/andreafey  |  linkedin.com/andreafey314159"
        elif opt in ("-m", "--misc"):
            print unicode(u"rhymes with \u03C0")

if __name__ == "__main__":
    sys.exit(main())
