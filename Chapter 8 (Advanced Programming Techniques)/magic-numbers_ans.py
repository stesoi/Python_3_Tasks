import os
import sys
import glob
import collections

class GetFunction:
    def __init(self):
        self.found_cache = {}
        self.not_found_cache = set()

    def __call__(self, module, function_name):
        function = self.found_cache.get((module, function_name), None)
        if function is None and (module, function_name) not in self.not_found_cache:
            try:
                function = getattr(module, function_name)
                if not isinstance(function, collections.Callable):
                    raise AttributeError()
                self.found_cache[module, function_name] = function
            except AttributeError:
                function = None
                self.not_found_cache.add((module, function_name))
        return function


def get_files(names):
    for name in names:
        if os.path.isfile(name):
            yield name
        else:
            for file in glob.iglob(name):
                if not os.path.isfile(file):
                    continue
                yield file


def load_modules():
    modules = []
    for name in os.listdir(os.path.dirname(__file__) or "."):
        if name.endswith(".py") and "magic" in name.lower():
            filename = name
            name = os.path.splitext(name)[0]
            if name.isidentifier() and name not in sys.modules:
                fh = None
                try:
                    fh = open(filename, "r", encoding="utf8")
                    code = fh.read()
                    module = type(sys)(name)
                    sys.modules[name] = module
                    exec(code, module.__dict__)
                    modules.append(module)
                except (EnvironmentError, SyntaxError) as err:
                    sys.modules.pop(name, None)
                    print(err)
                finally:
                    if fh is not None:
                        fh.close()
    return modules


def main():
    modules = load_modules()
    get_file_type_functions = []
    get_function = GetFunction()
    for module in modules:
        get_file_type = get_function(module, "get_file_type")
        if get_file_type is not None:
            get_file_type_functions.append(get_file_type)
    for file in get_files(sys.argv[1:]):
        fh = None
        try:
            fh = open(file, "rb")
            magic = fh.read(1000)
            for get_file_type in get_file_type_functions:
                filetype = get_file_type(magic, os.path.splitext(file)[1])
                if filetype is not None:
                    print("{0:.<20}{1}".format(filetype, file))
                    break
            else:
                print("{0:.<20}{1}".format("Unknown", file))
        except EnvironmentError as err:
            print(err)
        finally:
            if fh is not None:
                fh.close()

if __name__ == "__main__":
    main()