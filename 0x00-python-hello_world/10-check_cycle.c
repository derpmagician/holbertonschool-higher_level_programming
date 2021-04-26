#include <stdio.h>
#include <stddef.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: List
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *normal, *rapido;

	if (list == NULL)
		return (0);

	normal = rapido = list;

	while (normal && rapido && rapido->next)
	{
		rapido = rapido->next;
		rapido = rapido->next;
		slow = slow->next;

		if (normal = rapido)
			return (1);
	}

	return (0);
}
