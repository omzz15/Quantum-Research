def parse_args(args: str, min_args: int | None = None, max_args: int | None = None, no_flag = False) -> dict[str, list[str]]:
    """
    parses the arguments into tokens seperated by spaces and splitup by flags(anything with a - in front)

    Ex: parse_args("hello world -a -b these are --c args") will output:
    
    {
        "args": ['hello', 'world'],
        "-a": [],
        "-b": ['these', 'are'],
        "--c": ['args']
    }
    """
    tokens = filter(lambda s: not s == '', args.split(" "))
    
    lastflag = "args"
    parsed = {"args":[]}

    for t in tokens:
        if t[0] == '-':
            if no_flag:
                raise Exception("[ERROR] Flags are not allowed for this command!")
            lastflag = t
            if not t in parsed.keys():
                parsed[lastflag] = []
        else:
            parsed[lastflag].append(t)
            if max_args and lastflag == "args" and len(parsed["args"]) > max_args:
                raise Exception("[ERROR] Too many arguments were passed into this command! try running it again with fewer arguments")

    if min_args and len(parsed["args"]) < min_args:
        raise Exception("[ERROR] Too few arguments were passed into this command! try running it again with more arguments")

    return parsed

def validate_path_end(path : str) -> str:
    """
    Makes sure the path has a trailing /
    Ex: valudate_path_end("/home/etc") will return "/home/etc/" 
    """
    if not path[-1] == '/':
        path += '/'
    return path

def get_ending(value : str, seperator : str) -> str:
    return value[value.rindex(seperator) + 1:]

def remove_ending(value: str, seperator: str) -> str:
    return value[:value.rindex(seperator)]