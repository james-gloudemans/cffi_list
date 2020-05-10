#include <stdlib.h>
#include <util.h>
#include <list.h>

List create_list_node(void *data, size_t size)
{/* Construct and return a new list node */
    UTIL_ASSERT(data != NULL);
    List new_list_node = UTIL_NEW(List_t);
    new_list_node->next = new_list_node;
    new_list_node->prev = new_list_node;

    size_t node_size = size + 2*sizeof(List) + sizeof(void*);
    new_list_node->data = UTIL_malloc(node_size);
    if(new_list_node->data == NULL)
        abort();
    memcpy(new_list_node->data, data, node_size);

    return new_list_node;
}

void free_list_node(List node)
{/* Destroy a list node */
    UTIL_FREE(node->data);
    UTIL_FREE(node);
}

ListAnchor create_list()
{/* Create and return a new list. */
    ListAnchor list = UTIL_NEW(ListAnchor_t);
    list->next = list;
    list->prev = list;
    return list;
}

void free_list(ListAnchor list)
{/* Destroy a list */
    if(is_list_empty(list))
        return;
    List node = list;
    List next = list->next;
    while(node != NULL)
    {
        next = node->next;
        UTIL_FREE(node);
        node = next;
    }
}

UTIL_BOOL_t is_node_enqd(List node)
{/* Test if node is enqueued to a list already. */
    return (node->next == node ? UTIL_FALSE : UTIL_TRUE);
}

UTIL_BOOL_t is_list_empty(ListAnchor list)
{/* Test if list is empty */
    return (list->next == list ? UTIL_TRUE : UTIL_FALSE);
}

void push_head(ListAnchor list, List node)
{/* Push node to the front of the list. */
    UTIL_ASSERT(!is_node_enqd(node));
    List head = list->next;
    node->next = head;
    node->prev = list;
    head->prev = node;
    list->next = node;    
}

void push_tail(ListAnchor list, List node)
{/* Push node to the tail of the list. */
    UTIL_ASSERT(!is_node_enqd(node));
    List tail = list->prev;
    node->prev = tail;
    node->next = list;
    tail->next = node;
    list->prev = node;
}

List pop_head(ListAnchor list)
{/* Remove and return the head of the list */
    List head = list->next;
    list->next = head->next;
    head->next->prev = list;
    head->next = head;
    head->prev = head;
    return head;
}

List pop_tail(ListAnchor list)
{/* Remove and return the tail of the list */
    List tail = list->prev;
    list->prev = tail->prev;
    tail->prev->next = list;
    tail->next = tail;
    tail->prev = tail;
    return tail;
}

List peek_head(ListAnchor list)
{/* Return the head of the list */
    return list->next;
}

List peek_tail(ListAnchor list)
{/* Return the tail of the list. */
    return list->prev;
}

List dequeue_item(List node)
{/* Remove and return node from the list */
    node->prev->next = node->next;
    node->next->prev = node->prev;
    node->next = node;
    node->prev = node;
    return node;
}

List get(ListAnchor list, int i)
{/* Return the node from position i in the list. */
    if(is_list_empty(list))
        return NULL;
    List node;
    int j;
    for(node = list->next, j=0; node != list; node = node->next, ++j)
        if(j == i)
            return node;
    return NULL;
}

List get_reversed(ListAnchor list, int i)
{/* Return the node at position i traversing the list in reverse */
    if(is_list_empty(list))
        return NULL;
    List node;
    int j;
    for(node = list->prev, j=0; node != list; node = node->prev, ++j)
        if(j == i)
            return node;
    return NULL;
}

void insert(ListAnchor list, List node, const unsigned int i)
{/* Insert node in to list at position i */
    List next_node = get(list, i);
    if(next_node == NULL)
        push_tail(list, node);
    else
    {
        node->next = next_node;
        node->prev = next_node->prev;
        next_node->prev->next = node;
        next_node->prev = node;
    }
}

List get_next(List node)
{/* Return the next node in the list */
    return node->next;
}

List get_prev(List node)
{/* Return the previous node in the list */
    return node->prev;
}

void *get_data(List node)
{/* Return the data on the node */
    return node->data;
}

int get_len(ListAnchor list)
{/* Return the length of the list */
    List node = list->next;
    int len = 0;
    while(node != list)
    {
        node = node->next;
        ++len;
    }
    return len;
}
