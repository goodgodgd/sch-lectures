#ifndef CPP_FUNCTIONS_H
#define CPP_FUNCTIONS_H

#include <iostream>
using namespace std;

void declareVariableAnywhere()
{
    cout << endl << "===== declareVariableAnywhere =====" << endl;
    int a = 1;
    a += 3;
    float b = 3.14f;
    b += 9.9f;
    cout << "declare variable anywhere: " << a << " " << b << endl;
    cout << "declare variable inside 'for' line" << endl;
    for(int c=0; c<10; c++)
        cout << c << ", ";
    cout << endl;
}

void useBoolType()
{
    cout << endl << "===== boolTypeIsAvailable =====" << endl;
    bool doYouLikeOrange = false;
    int orange = 5;
    cout << "use bool type for condition check: " << doYouLikeOrange
              << " " << (orange>3) << endl;
}

void useStructWithoutStruct()
{
    cout << endl << "===== useStructWithoutStruct =====" << endl;
    struct Fruit
    {
        char* name = "apple";
        int age = 1;
        float weight = 0.1f;
    };

    // C style
    // struct Fruit apple;
    // C++ style
    Fruit apple;
    cout << "declare struct instance without 'struct' tag: " << apple.name << endl;
}

void casting()
{
    cout << endl << "===== casting =====" << endl;
    float a=1.4f, b=10.89f;
    int wrap_varialbe = int(a);
    int wrap_type = (int)a;
    int wrap_both = (int)(a);

    cout << "casting a: " << "(type)variable: " << wrap_varialbe
              << ", type(variable): " << wrap_type
              << ", (type)(variable): " << wrap_both << endl;
    cout << "casting b: " << "(type)variable: " << (int)b
              << ", type(variable): " << int(b)
              << ", (type)(variable): " << (int)(b) << endl;
    cout << "all of three castings work fine"
              << " but type(variable) is recommended" << endl;
}

void newAndDeleteSimple()
{
    cout << endl << "===== newAndDeleteSimple =====" << endl;
    // 포인터: 객체가 생성된 메모리 주소
    int* ptr = new int;
    *ptr = 10;
    cout << "simply create int: " << ptr << " " << *ptr << endl;
    delete ptr;
}

void newAndDelete1DArray()
{
    cout << endl << "===== newAndDelete1DArray =====" << endl;
    int* mem = new int[10];
    for(int i=0; i<10; i++)
        mem[i] = i;
    cout << "allocate 1D array by new: " << mem << " "
              << mem[0] << " " << mem[9] << endl;
    delete[] mem;
    cout << "deallocate 1D array by delete[]" << endl;
}

void newAndDelete2DArray()
{
    cout << endl << "===== newAndDelete2DArray =====" << endl;
    cout << "allocate 2D array of int: int[10][20]" << endl;
    cout << "allocate int*[10] first, then allocate int[20] for each int*[10]" << endl;
    int** mem2D = new int*[10];
    for(int i=0; i<10; i++)
        mem2D[i] = new int[20];

    cout << "deallocate 2D array: delete each int[20], then delete int*[10]" << endl;
    for(int i=0; i<10; i++)
        delete[] mem2D[i];
    delete[] mem2D;
}


void _noswap(int a, int b)
{
    int t = a;
    a = b;
    b = t;
}

void _swapByRef(int& a, int& b)
{
    int t = a;
    a = b;
    b = t;
}

void _swapByPtr(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

void callByReference()
{
    cout << endl << "===== callByReference =====" << endl;
    int a=10, b=200;
    cout << "before swap  a=" << a << ", b=" << b << endl;

    _noswap(a, b);
    cout << "after _noswap a=" << a << ", b=" << b << endl;
    _swapByRef(a, b);
    cout << "after _swapByRef " << a << ", b=" << b << endl;
    _swapByPtr(&a, &b);
    cout << "after _swapByPtr " << a << ", b=" << b << endl;

    // NOT allowed
    // swap(10, 200);
    // swap(a, 200);
    // swap(10, b);
}

void _defaultArgFunc(int a, char* b="hello", float c=11.1f)
{
    cout << "value: " << a << " " << b << " " << c << endl;
}

void defaultArgument()
{
    cout << endl << "===== defaultArgument =====" << endl;
    _defaultArgFunc(10);
    _defaultArgFunc(10, "hihi~");
    _defaultArgFunc(10, "happy", 21.5f);
}

void functionOverloading()
{
    cout << endl << "===== functionOverloading(1) =====" << endl;
    cout << "empty input argument" << endl;
}

void functionOverloading(int a, float b)
{
    cout << endl << "===== functionOverloading(2) =====" << endl;
    cout << "input arguments: " << a << " " << b << endl;
}

#endif // CPP_FUNCTIONS_H
