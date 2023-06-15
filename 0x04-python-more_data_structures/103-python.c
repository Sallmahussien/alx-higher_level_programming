#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print a python lis
 * p: PyObject python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_length = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_length);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
}

/**
 * print_python_bytes - 
 * p: 
 */
void print_python_bytes(PyObject *p)
{
}
