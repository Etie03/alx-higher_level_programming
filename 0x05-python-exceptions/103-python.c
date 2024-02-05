#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_hex(const char *stg, int n);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject
 */
void print_python_list(PyObject *p)
{
	int m = 0, list_len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_len = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; m < list_len; ++m)
	{
		item = PyList_GET_ITEM(p, m);
		printf("Element %d: %s\n", m, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}

	fflush(stdout);
}

/**
 * print_python_bytes - prints info about python bytes
 * @p: address of pyobject struct
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *) p;
	int calc_bytes, clone_size = 0;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	clone_size = PyBytes_Size(p);
	calc_bytes = clone_size + 1;

	if (calc_bytes >= 10)
		calc_bytes = 10;

	printf("  size: %d\n", clone_size);
	printf("  trying string: %s\n", clone->ob_sval);
	printf("  first %d bytes: ", calc_bytes);
	print_hexn(clone->ob_sval, calc_bytes);
	printf("\n");

	fflush(stdout);
}

/**
 * print_python_float - prints info about python float
 * @p: address of pyobject struct
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *clone = (PyFloatObject *) p;
	float n = 0;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	n = clone->ob_fval;

	if ((int) n == n)
		printf("  value: %0.1f\n", clone->ob_fval);
	else
		printf("  value: %0.16g\n", clone->ob_fval);

	fflush(stdout);
}

/**
 * print_hex - prints hexadecimal
 * @stg: the string
 * @n: the integer
 */
void print_hex(const char *stg, int n)
{
	int m = 0;

	for (; m < n - 1; ++m)
		printf("%02x ", (unsigned char) stg[m]);

	printf("%02x", stg[m]);
	fflush(stdout);
}
