all: test list

remake: clean all

liblist.so: list.o util.o
	gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic -I . $^

test: test.o util.o list.o
	gcc -o test test.o util.o list.o

list: liblist.so
	./build_list.py

clean:
	rm -f test *.o *.so _list_cffi.c