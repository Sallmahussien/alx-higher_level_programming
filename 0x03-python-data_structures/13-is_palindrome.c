#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * listint_len - the number of elements in a linked listint_t list.
 * @h: pointer to head of the list
 * Return: no. of list elements
 */
int listint_len(listint_t *h)
{
	int nodes = 0;
	listint_t *tmp = h;

	while (tmp)
	{
		nodes++;
		tmp = tmp->next;
	}
	return (nodes);
}

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to the list head address
 * Return:  pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *tmp2 = *head;
	int size = listint_len(*head), i;

	if (!(*head) || !head)
		return (1);

	for (i = 0; i < (size % 2 == 0 ? size / 2 : size / 2 + 1); i++)
		tmp2 = tmp2->next;
	rev = reverse_listint(&tmp2);

	tmp = *head;
	for (i = 0; i < size / 2; i++)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}

	return (1);
}
