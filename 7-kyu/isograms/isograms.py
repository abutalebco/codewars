import re
isogram_process = re.compile(r"^(?:([a-zA-Z])(?!.*\1)|[-])*$", re.IGNORECASE)
def is_isogram(string):
    return bool(isogram_process.match(string))