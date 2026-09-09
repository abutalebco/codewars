import re
def solution(s):
    return re.sub(r"([A-Z])", r" \1", s)