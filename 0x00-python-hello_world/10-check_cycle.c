#include "lists.h"

/**
 * check_cycle - This is a function that
 * checks if a linked list contains a cycle
 * @list: A pointer argument that linked list to check
 *
 * Return:Return a value 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr = list;
	listint_t *pt = list;

	while (ptr && pt && pt->next)
	{
		ptr = ptr->next;
		pt = pt->next->next;
		if (ptr == pt)
			return (1);
	}

	return (0);
}
