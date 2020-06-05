"""linkedlistc.py: circular doubly linked list."""
import sys
from typing import Generic, Iterable, Iterator, Optional, TypeVar, Union

from clist._list_cffi import ffi, lib

T = TypeVar("T")


class LinkedList(Generic[T]):
    """Circular doubly-linked list."""

    def __init__(self, iterable: Optional[Iterable] = None) -> None:
        """Initialize an new linked list."""
        # Anchor node for the list
        self._clist = lib.create_list()
        # python nodes need to persist to handle casting of void *
        self._nodes = set()

        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __repr__(self) -> str:
        """Return repr(self)."""
        return str(self)

    def __str__(self) -> str:
        """Return str(self)."""
        return "LinkedList(" + ", ".join(str(data) for data in self) + ")"

    def __bool__(self) -> bool:
        """Return bool(self)."""
        return not bool(lib.is_list_empty(self._clist)[0])

    def __iter__(self) -> Iterator[T]:
        """
        Return iter(self).

        This might be improved by implementing a coroutine in the C library.
        """
        node = lib.peek_head(self._clist)
        while node != self._clist:
            yield ffi.from_handle(node.data)
            node = lib.get_next(node)

    def __len__(self) -> int:
        """Return len(self)."""
        return lib.get_len(self._clist)

    def __getitem__(self, i: int) -> T:
        """Return self[i]. No slicing."""
        if isinstance(i, slice):
            raise NotImplementedError
        if i < 0:
            node_i = lib.get_reversed(self._clist, -(i + 1))
        else:
            node_i = lib.get(self._clist, i)
        return ffi.from_handle(node_i.data)

    def __contains__(self, item: T) -> bool:
        """Return item in self."""
        for data in self:
            if data == item:
                return True
        return False

    def index(self, item: T) -> Union[int, None]:
        """Return first index where item is stored, or None if it is not in the list."""
        for i, data in enumerate(self):
            if data == item:
                return i
        return None

    def count(self, item: T) -> int:
        """Return number of times item appears in the list."""
        result: int = 0
        for data in self:
            if data == item:
                result += 1
        return result

    def insert(self, i: int, item: T) -> None:
        """Insert item into list at position i."""
        size = sys.getsizeof(item)
        node = ffi.new_handle(item)
        list_node = lib.create_list_node(node, size)
        self._nodes.add(list_node)
        lib.insert(self._clist, list_node, i)

    def appendleft(self, item: T) -> None:
        """Append item to the left side of the list."""
        size = sys.getsizeof(item)
        node = ffi.new_handle(item)
        list_node = lib.create_list_node(node, size)
        self._nodes.add(list_node)
        lib.push_head(self._clist, list_node)

    def append(self, item: T) -> None:
        """Append item to the right side of the list."""
        size = sys.getsizeof(item)
        node = ffi.new_handle(item)
        list_node = lib.create_list_node(node, size)
        self._nodes.add(list_node)
        lib.push_tail(self._clist, list_node)

    def popleft(self) -> T:
        """Remove and return from the left side of the list."""
        node = lib.pop_head(self._clist)
        result = ffi.from_handle(node.data)
        self._nodes.remove(node)
        return result

    def pop(self) -> T:
        """Remove and return from the right side of the list."""
        node = lib.pop_tail(self._clist)
        result = ffi.from_handle(node.data)
        self._nodes.remove(node)
        return result


if __name__ == "__main__":
    mylist = LinkedList[str]()
    mylist.append("James")
    mylist.append("Samantha")
    mylist.append("Newton")
    print(mylist)
    # print(3 in mylist)
    # print(f"len: {len(mylist)}")
    # for item in mylist:
    #     print(item)
    # print(f"len: {len(mylist)}")
    # for i in range(len(mylist)):
    #     print(mylist[i])
    # print(f"len: {len(mylist)}")
    # while mylist:
    #     print(mylist.popleft())
    # print(f"len: {len(mylist)}")
