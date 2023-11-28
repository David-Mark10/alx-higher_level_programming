#include "lists.h"

/**
 * check_cycle - This function checks if
 * a linked list contains a cycle
 * @list: It is argument that linked list to check
 *
 * Return: return 1 if the list contain a cycle, 0 if it doesn't
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
