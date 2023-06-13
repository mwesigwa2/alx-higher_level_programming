#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to python object
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	int x;
	PyListObject *list = (PyListObject *)p;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (x = 0; x < size; x++)
		printf("Element %d: %s\n", x, Py_TYPE(list->ob_item[x])->tp_name);
}
