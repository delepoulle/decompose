# decompose.py

import sys
from typing import List

def decompose(n: int) -> List[int] :
    return [1]

def main():
    print("start")
    n = sys.argv[1]
    print("nombre à décomposer",n)
    print(decompose(n))


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit