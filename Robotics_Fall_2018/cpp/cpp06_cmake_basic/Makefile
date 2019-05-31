myapp: main.o foo.o bar.o
	g++ -o myapp main.o foo.o bar.o
main.o: foo.h bar.h main.cpp
foo.o: foo.h foo.cpp
bar.o: bar.h bar.cpp
