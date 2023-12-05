#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t dize, j;
    PyObject *ptr;

    dize = Py_SIZE(p);

    printf("[*] Size of the Python List = %ld\n", dize);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (j = 0; j < dize; j++)
    {
        printf("Element %ld: ", j);
        ptr = PyList_GetItem(p, j);
        printf("%s\n", ptr->ob_type->tp_name);
    }
}
