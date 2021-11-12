import random
import string


class RandString:

    def generate(prefix="",length=10):
        strg = ''.join(random.choice(string.ascii_lowercase)
                       for _ in range(length))
        return prefix + strg
