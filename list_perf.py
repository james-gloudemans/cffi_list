import random
import string
from collections import deque
from timeit import timeit
from linkedlistc import LinkedList as LLC
from linkedlist import LinkedList as LLP

if __name__ == "__main__":

    def rand_str(
        length: int, alphabet: int = string.ascii_letters + string.digits
    ) -> str:
        """Return a random string of specifiend `length` from `alphabet`."""
        return "".join((random.choice(alphabet) for _ in range(length)))

    N = 100000
    pylist = deque(rand_str(random.randrange(10, 100)) for _ in range(N))
    llc = LLC(pylist)
    llp = LLP(pylist)

    print("Peek left:")
    print(f"{timeit(lambda: pylist[0], number=1000): .3e}")
    print(f"{timeit(lambda: llc[0], number=1000): .3e}")
    print(f"{timeit(lambda: llp[0], number=1000): .3e}")
    print()

    print("Peek right:")
    print(f"{timeit(lambda: pylist[-1], number=1000): .3e}")
    print(f"{timeit(lambda: llc[-1], number=1000): .3e}")
    print(f"{timeit(lambda: llp[-1], number=1000): .3e}")
    print()

    print("random access: ")
    print(f"{timeit(lambda: pylist[random.randrange(0, N)], number=1000): .3e}")
    print(f"{timeit(lambda: llc[random.randrange(0, N)], number=1000): .3e}")
    print(f"{timeit(lambda: llp[random.randrange(0, N)], number=1000): .3e}")
    print()

    print("Pop left")
    print(f"{timeit(lambda: pylist.popleft(), number=1000): .3e}")
    print(f"{timeit(lambda: llc.popleft(), number=1000): .3e}")
    print(f"{timeit(lambda: llp.popleft(), number=1000): .3e}")
    print()

    print("pop right:")
    print(f"{timeit(lambda: pylist.pop(), number=1000): .3e}")
    print(f"{timeit(lambda: llc.pop(), number=1000): .3e}")
    print(f"{timeit(lambda: llp.pop(), number=1000): .3e}")
    print()
