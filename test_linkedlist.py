"""test_linkedlist.py: Tests for linkedlist.py."""

from linkedlistc import LinkedList


def test_build():
    """Test building LinkedList from list."""
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList(lst)
    for a, b in zip(lst, ll):
        assert a == b


def test_append():
    """Test building list by repeated append."""
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList()
    for x in lst:
        ll.append(x)
    for a, b in zip(lst, ll):
        assert a == b


def test_appendleft():
    """Test building list by repeated appendleft."""
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList()
    for x in reversed(lst):
        ll.appendleft(x)
    for a, b in zip(lst, ll):
        assert a == b


def test_insert():
    """Test insert method."""
    lst = [0, 1, 2, 3, 4, 5]
    ll = LinkedList()
    ll.append(1)
    ll.append(5)
    for x in [2, 3, 4]:
        ll.insert(x - 1, x)
    ll.insert(0, 0)
    for a, b in zip(lst, ll):
        assert a == b


def test_len():
    """Test __len__."""
    lst = []
    ll = LinkedList()
    for i in range(5):
        lst.append(i)
        ll.append(i)
        assert len(ll) == len(lst)


def test_reversed():
    """Test __reversed__."""
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList(lst)
    for a, b in zip(reversed(lst), reversed(ll)):
        assert a == b


def test_getitem():
    """Test __getitem__."""
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList(lst)
    for i, x in enumerate(lst):
        assert ll[i] == x
    for i, x in enumerate(reversed(lst)):
        assert ll[-(i + 1)] == x


def test_contains():
    """Test __contains__."""
    lst = [1, 2, 3, 4, 5]
    ll = LinkedList(lst)
    for x in lst:
        assert x in ll


def test_index():
    """Test index() method."""
    lst = [0, 1, 2, 3, 4]
    ll = LinkedList(lst)
    for x in lst:
        assert ll.index(x) == x


def test_count():
    """Test count() method."""
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    ll = LinkedList(lst)
    for x in lst:
        assert ll.count(x) == x


if __name__ == "__main__":
    test_build()
    test_append()
    test_appendleft()
    test_insert()
    test_len()
    test_reversed()
    test_getitem()
    test_contains()
    test_index()
    test_count()
