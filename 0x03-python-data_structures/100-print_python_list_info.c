#include <Python.h>

/**
 * print_python_list_info - prints some information about python lits
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_length = PyList_Size(p), idx;
	PyObject *list_item;

	printf("[*] Size of the Python List = %ld\n", list_length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (idx = 0; idx < list_length; idx++)
	{
		list_item = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(list_item)->tp_name);
	}
}
