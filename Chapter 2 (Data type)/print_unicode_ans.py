import sys
import unicodedata

def print_unicode_table(word):
    print("decimal  hex  chr {0:^40}".format("name"))
    print("------- ----- --- {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while (code < end):
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        in_string = 0
        for word in words:
            if(word in name.lower()):
                in_string += 1
        if (len(words) == 0 or len(words) == in_string):
            print("{0:7} {0:5X} {0:^3c} {1}".format(code, name.title()))
        code += 1

words = []

if (len(sys.argv) > 1):
    if (sys.argv[1] in ("-h", "--help")):
        print("usage: {0} [string]".format(sys.argv[0]))
        words = None
    else:
        for i in range(len(sys.argv)-1):
            words.append(sys.argv[i+1].lower())

if (words != None):
    print_unicode_table(words)