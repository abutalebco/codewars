import re
import math
def entropy(password):
    # your code
    if not password:
        return 0
    
    pool_size = 0
    
    if re.search(r"[a-z]", password):
        pool_size += 26
    if re.search(r"[A-Z]", password):
        pool_size += 26
    if re.search(r"[0-9]", password):
        pool_size += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool_size += 32
        
    return len(password) * math.log2(pool_size)