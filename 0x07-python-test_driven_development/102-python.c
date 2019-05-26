#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_sting - prints info about python strings
 * @p: address of pyobject struct
 */
void print_python_string(PyObject *p)
{
	wchar_t *wstr;

	setlocale(LC_CTYPE,"en_US.UTF-8");
    fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("  value: ");
	fflush(stdout);
	wstr = PyUnicode_AS_UNICODE(p);
	while (*wstr)
		putwchar(*wstr++);
	putchar('\n');
	fflush(stdout);
}
