import sys
import xml.sax.saxutils

def process_options():
    maxwidth, format = (100, ".0f")
    if(len(sys.argv)>1):
        if(sys.argv[1] in ("-h", "--help")):
            maxwidth, format = (None, None)
            print("usage:\n",
                  "csv2html.py [maxwidth = int] [format = str] < infile.csv > outfile.html\n",
                  "maxwidth is an optional integer; if specified, it sets the maximum number of characters "
                  "that can be output for string fields, otherwise a default of 100 characters is used.\n",
                  'format is the format to use for numbers; if not specified it defaults to ".0f".')
        else:
            try:
                maxwidth = int(sys.argv[1][sys.argv[1].index('=')+1:])
                if(len(sys.argv)>2):
                    format = sys.argv[2][sys.argv[2].index('=')+1:]
            except ValueError as err:
                print(err)
    return maxwidth, format

def main():
    maxwidth, format = process_options()
    if(maxwidth!=None and format!=None):
        print_start()
        count = 0
        while True:
            try:
                line = input()
                if (count == 0):
                    color = "lightgreen"
                elif (count % 2):
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, format)
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if (not field):
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x), format))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = xml.sax.saxutils.escape(field)
                if (len(field) <= maxwidth):
                    print("<td>{0}</td>".format(field))
                else:
                    print("<td>{0:.{1}} ...</td>".format(field, maxwidth))
    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if (quote is None): # начало строки в кавычках
                quote = c
            elif quote == c: # конец строки в кавычках
                quote = None
            else:
                field += c # другая кавычка внутри строки в кавычках
            continue
        if (quote is None and c == ","): # end of field
            fields.append(field)
            field = ""
        else:
            field += c # добавить символ в поле
    if (field):
        fields.append(field) # добавить последне поле в список
    return fields

def print_end():
    print("</table>")

main()