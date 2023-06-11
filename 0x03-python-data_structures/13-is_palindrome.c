#include "lists.h"

listint_t *reverse_listint(listint_t **head);

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: pointer to the list head address
 * Return:  pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *ahead, *behind;

	if (head == NULL || *head == NULL)
		return (NULL);

	behind = NULL;

	while ((*head)->next != NULL)
	{
		ahead = (*head)->next;
		(*head)->next = behind;
		behind = *head;
		*head = ahead;
	}

	(*head)->next = behind;

	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of a linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev;

	if (!*head || !(*head)->next || !head)
		return (1);

	tmp = *head;
	rev = reverse_listint(&*head);
	while (tmp)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	return (1);
}
