def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') or s.lower().count('x') == 0 and s.lower().count('o') == 0 else False