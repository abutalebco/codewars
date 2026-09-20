def sponge_meme(str):
    return "".join([char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(str)])