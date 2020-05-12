"""linkedlist.py:  circular doubly linked list."""
# standard library
from collections.abc import MutableSequence
from typing import Any, Generic, Iterable, Iterator, Optional, TypeVar, Union

# third party libraries

# local libraries

T = TypeVar("T")


class LinkedList(Generic[T], MutableSequence):
    """A circular doubly linked list."""

    class Node(object):
        """A node in the list."""

        def __init__(
            self,
            data: T,
            prev_node: Optional["Node"] = None,
            next_node: Optional["Node"] = None,
        ) -> None:
            """Initialize a node."""
            self.prev: Optional["Node"] = prev_node
            self.next: Optional["Node"] = next_node
            self.data: T = data

    def __init__(self, iterable: Optional[Iterable] = None) -> None:
        """Initialize linked list object."""
        self.head = None
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __repr__(self) -> str:
        """Return repr(self)."""
        return f"<LinkedList at {hex(id(self.head))}>"

    def __str__(self) -> str:
        """Return str(self)."""
        return str(list(self))

    def __len__(self) -> int:
        """Return len(self)."""
        result: int = 0
        for item in self:
            result += 1
        return result

    def __iter__(self) -> Iterator[Any]:
        """Return iter(self)."""
        if self.head is None:
            return None
        yield self.head.data
        node = self.head.next
        while node is not self.head:
            yield node.data
            node = node.next

    def __reversed__(self) -> Iterator[T]:
        """Return reversed(self)."""
        if self.head is None:
            return None
        else:
            node = self.head.prev
            yield self.head.prev.data
            while node is not self.head:
                node = node.prev
                yield node.data

    def __getitem__(self, i) -> T:
        """Return self[i]."""
        if self.head is None:
            raise IndexError("LinkedList index out of bounds")
        if isinstance(i, slice):
            raise NotImplementedError
        if i < 0:
            it = enumerate(reversed(self))
            i = -(i + 1)
        else:
            it = enumerate(iter(self))
        for j, item in it:
            if j == i:
                return item
        raise IndexError("LinkedList index out of bounds")

    def __contains__(self, item: T) -> bool:
        """Return item in self."""
        for data in self:
            if data == item:
                return True
        return False

    def __setitem__(self, i, item: Union[T, Iterable[T]]) -> None:
        """Replace item at position i with item."""
        raise NotImplementedError

    def __delitem__(self, i) -> None:
        """Remove the item at position i from the list."""
        raise NotImplementedError

    def insert(self, i: int, item: T) -> None:
        """Insert item into list at position i."""
        if self.head is None:
            self._add_to_empty(item)
        elif i == 0:
            self.appendleft(item)
        else:
            for (j, node) in enumerate(self._nodes()):
                if j == i:
                    prev_node = node.prev
                    in_node = self.Node(item, prev_node, node)
                    prev_node.next = in_node
                    node.prev = in_node

    # TODO: More mixins for MutableSequence

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

    def append(self, item: T) -> None:
        """Append `item` to the right end of the list."""
        if self.head is None:
            self._add_to_empty(item)
        else:
            tail = self.head.prev
            new_tail = self.Node(item, tail, self.head)
            tail.next = new_tail
            self.head.prev = new_tail

    def appendleft(self, item: T) -> None:
        """Append `item` to the left end of the list."""
        if self.head is None:
            self._add_to_empty(item)
        else:
            old_head = self.head
            self.head = self.Node(item, old_head.prev, old_head)
            old_head.prev.next = self.head
            old_head.prev = self.head

    def pop(self) -> T:
        """Remove and return from the right side of the list."""
        node = self.head.prev
        self.head.prev = node.prev
        node.prev.next = self.head
        return node.data

    def popleft(self) -> T:
        """Remove and return from the left side of the list."""
        node = self.head
        node.next.prev = node.prev
        node.prev.next = node.next
        self.head = node.next
        return node

    def _add_to_empty(self, item: T) -> None:
        """Add `item` to empyt list."""
        self.head = self.Node(item)
        self.head.next = self.head
        self.head.prev = self.head

    def _nodes(self) -> Optional[Iterator["LinkedList"]]:
        """Iterator over the nodes in the list."""
        if self.head is None:
            return None
        yield self.head
        node = self.head.next
        while node is not self.head:
            yield node
            node = node.next


if __name__ == "__main__":

    lst = LinkedList([1, 2, 3, 4, 5])
    for node in lst:
        print(node)
