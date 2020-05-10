#!/usr/bin/python3
from cffi import FFI

builder = FFI()

builder.cdef(
    """
typedef char UTIL_BOOL_t;

// Node in a doubly-linked list
typedef struct list_node
{
    struct list_node *next;
    struct list_node *prev;
    void *data;

} List_t, *List;

// Construct and return a new list node.
List create_list_node(void *data, size_t size);

// Destroy a list node.
void free_list_node(List node);

// An anchor for a circular doubly-linked list
typedef List_t ListAnchor_t, *ListAnchor;

// Create and return a new list
ListAnchor create_list(void);

// Destroy a list
void free_list(ListAnchor list);

// Is the node enqueued in a list?
UTIL_BOOL_t is_node_enqd(List node);

// Is the list empty?
UTIL_BOOL_t is_list_empty(ListAnchor list);

// Push node to head of the list
void push_head(ListAnchor list, List node);

// Push node to tail of the list
void push_tail(ListAnchor list, List node);

// Remove and return the head
List pop_head(ListAnchor list);

// Remove and return the tail
List pop_tail(ListAnchor list);

// Return the head
List peek_head(ListAnchor list);

//Return the tail
List peek_tail(ListAnchor list);

// Remove and return the node from the list
List dequeue_item(List node);

// Return the node at position i in the list
List get(ListAnchor list, int i);

// Return the node at position i traversing the list in reverse
List get_reversed(ListAnchor, int i);

// Insert node in to list at position i
void insert(ListAnchor list, List node, const unsigned int i);

// Return the next node in the list
List get_next(List node);

// Return the previous node in the list
List get_prev(List node);

// Return the data on the node
void *get_data(List node);

// Return the length of the list
int get_len(ListAnchor list);
"""
)

builder.set_source(
    "_list_cffi",
    """
#include "util.h"
#include "list.h"
""",
    libraries=["list"],
    library_dirs=["/home/james/projects/cffi_list/clist"],
    extra_link_args=["-Wl,-rpath=" + "/home/james/projects/cffi_list/clist"],
)

if __name__ == "__main__":
    builder.compile(verbose=True)
