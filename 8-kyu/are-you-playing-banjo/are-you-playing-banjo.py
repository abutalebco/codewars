import re
def are_you_playing_banjo(name):
    # Implement me!
    if re.search(r"\b[rR]\w", name):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
​