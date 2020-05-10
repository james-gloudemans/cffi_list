#include <stdio.h>
#include <stdlib.h>
#include <util.h>
#include <list.h>

typedef struct
{
    char *first_name;
    char *last_name;
    int age;
} Person_t, *Person;

Person create_person(const char *first_name, const char *last_name, const int age)
{
    UTIL_ASSERT(first_name != NULL && last_name != NULL);
    Person new_person = UTIL_NEW(Person_t);
    new_person->first_name = UTIL_NEW_STR_IF(first_name);
    new_person->last_name = UTIL_NEW_STR_IF(last_name);
    new_person->age = age;

    return new_person;
}

void free_person(Person person)
{
    UTIL_ASSERT(person != NULL);
    UTIL_FREE(person->first_name);
    UTIL_FREE(person->last_name);
    UTIL_FREE(person);
}

void print_person(Person person)
{
    printf("%s %s, %d yrs\n", person->first_name, person->last_name, person->age);
}

void print_list_of_persons(ListAnchor list)
{
    List node = list->next;
    while(node != list)
    {
        print_person((Person)(node->data));
        node = node->next;
    }
}

int main(int argc, char *argv[])
{
    Person me = create_person("James", "Gloudemans", 30);
    Person her = create_person("Sami", "Beikman", 31);
    Person newt = create_person("Newton", "Gloudemans", 3);
    ListAnchor list = create_list();
    push_tail(list, create_list_node(me, sizeof(*me)));
    push_tail(list, create_list_node(her, sizeof(*her)));
    insert(list, create_list_node(newt, sizeof(*newt)), 3);
    
    while(!is_list_empty(list))
    {
        print_person((Person)pop_head(list)->data);
    }
    
    return 0;
}