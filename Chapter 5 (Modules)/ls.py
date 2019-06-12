# with https://github.com/BaneZhang/python/blob/master/Programming_in_Python3/Examples/ls.py

import datetime
import optparse
import os

def process_options():
    parser = optparse.OptionParser(usage="%prog [options] [path1 [path2 [... pathN]]]\n" +
                                         "The paths are optional; if not given . is used.") # создаём парсер
    # добавляем аругменты командной строки
    parser.add_option("-H", "--hidden",
                      dest="hidden",
                      action="store_true",
                      help="show hidden files [default: off]")
    parser.add_option("-m", "--modified",
                      dest="modified",
                      action="store_true",
                      help="show last modified date/time [default: off]")
    orderlist = ["name", "n", "modified", "m", "size", "s"]
    parser.add_option("-o", "--order",
                      dest="order",
                      choices=orderlist,
                      help="order by ({0}) [default: %default]".format(
                          ", ".join(["'" + x + "'" for x in orderlist])))
    parser.add_option("-r", "--recursive",
                      dest="recursive",
                      action="store_true",
                      help="recurse into subdirectories [default: off]")
    parser.add_option("-s", "--sizes",
                      dest="sizes",
                      action="store_true",
                      help="show sizes [default: off]")
    parser.set_defaults(order=orderlist[0])
    opts, args = parser.parse_args() # получение аргументов
    args = args if args else ["."]
    return opts, args

def main():
    number_of_files, number_of_dirs = (0, 0) # счётчики количества файлов и директорий
    opts, paths = process_options() # определение переданных параметров
    if not opts.recursive:
        filenames = []
        dirnames = []
        for path in paths:
            if os.path.isfile(path):
                filenames.append(path)
                continue
            for name in os.listdir(path):
                if not opts.hidden and name.startswith("."):
                    continue
                fullname = os.path.join(path, name)
                if fullname.startswith("./"):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    dirnames.append(fullname)
        number_of_files += len(filenames)
        number_of_dirs += len(dirnames)
        process_lists(opts, filenames, dirnames)
    else:
        for path in paths:
            for root, dirs, files in os.walk(path):
                if not opts.hidden:
                    dirs[:] = [dir for dir in dirs
                               if not dir.startswith(".")]
                filenames = []
                for name in files:
                    if not opts.hidden and name.startswith("."):
                        continue
                    fullname = os.path.join(root, name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    filenames.append(fullname)
                number_of_files += len(filenames)
                number_of_dirs += len(dirs)
                process_lists(opts, filenames, [])
    print("{0} file{1}, {2} director{3}".format(
          "{0:n}".format(number_of_files) if number_of_files else "no",
          "s" if number_of_files != 1 else "",
          "{0:n}".format(number_of_dirs) if number_of_dirs else "no",
          "ies" if number_of_dirs != 1 else "y"))


def process_lists(opts, filenames, dirnames):
    keys_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                                os.path.getmtime(name))
                                    .isoformat(" ")[:19] + " ")
            except EnvironmentError:
                modified = "{0:>19} ".format("unknown")
        size = ""
        if opts.sizes:
            try:
                size = "{0:>15n} ".format(os.path.getsize(name))
            except EnvironmentError:
                size = "{0:>15} ".format("unknown")
        if os.path.islink(name):
            name += " -> " + os.path.realpath(name)
        if opts.order in {"m", "modified"}:
            orderkey = modified
        elif opts.order in {"s", "size"}:
            orderkey = size
        else:
            orderkey = name
        keys_lines.append((orderkey, "{modified}{size}{name}".format(
                                     **locals())))
    size = "" if not opts.sizes else " " * 15
    modified = "" if not opts.modified else " " * 20
    for name in sorted(dirnames):
        keys_lines.append((name, modified + size + name + "/"))
    for key, line in sorted(keys_lines):
        print(line)

if __name__ == "__main__":
    main()
