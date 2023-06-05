#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int search(listint_t *node, listint_t **arr, int arr_len);
void append(listint_t *node, listint_t **arr, int *arr_len);

/**
 * search - search for pointer node in array arr
 * @node: pointer to node
 * @arr: array
 * @arr_len: array length
 * Return: 1 if array has node, 0 otherwise
 */
int search(listint_t *node, listint_t **arr, int arr_len)
{
	int i;

	for (i = 0; i < arr_len; i++)
		if (node == arr[i])
			return (1);

	return (0);

}

/**
 * append - append node at the end of an array
 * @node:
 * @arr:
 * @arr_len:
 */
void append(listint_t *node, listint_t **arr, int *arr_len)
{
	arr =  realloc(arr, sizeof(listint_t *) * (*arr_len + 1));
	arr[*arr_len ] = node;
	(*arr_len)++;
}

/**
 * check_cycle - checks if linked list has a cycle or not
 * @list: linked list
 * Return: 1 if it has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t **arr = malloc(sizeof(listint_t *));
	int arr_len = 0;

	while (current)
	{
		if (search(current, arr, arr_len) == 1)
		{
			free(arr);
			return (1);
		}
		else
		{
			append(current, arr, &arr_len);
		}
		current = current->next;
	}

	free(arr);
	return (0);
}
