#include "cpp_functions.h"

int main()
{
    std::cout << "Hello Students!" << std::endl;

    declareVariableAnywhere();

    useBoolType();

    useStructWithoutStruct();

    casting();

    newAndDeleteSimple();
    newAndDelete1DArray();
    newAndDelete2DArray();

    callByReference();

    defaultArgument();

    functionOverloading();
    functionOverloading(1, 3.1f);

    return 0;
}

/* Program output

Hello Students!

===== declareVariableAnywhere =====
declare variable anywhere: 4 13.04
declare variable inside 'for' line
0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

===== boolTypeIsAvailable =====
use bool type for condition check: 0 1

===== useStructWithoutStruct =====
declare struct instance without 'struct' tag: apple

===== casting =====
casting a: (type)variable: 1, type(variable): 1, (type)(variable): 1
casting b: (type)variable: 10, type(variable): 10, (type)(variable): 10
all of three castings work fine but type(variable) is recommended

===== newAndDeleteSimple =====
simply create int: 10

===== newAndDelete1DArray =====
allocate 1D array by new: 0x667050 0 9
deallocate 1D array by delete[]

===== newAndDelete2DArray =====
allocate 2D array of int: int[10][20]
allocate int*[10] first, then allocate int[20] for each int*[10]
deallocate 2D array: delete each int[20], then delete int*[10]

===== callByReference =====
before swap  a=10, b=200
after _noswap a=10, b=200
after _swapByRef 200, b=10
after _swapByPtr 10, b=200

===== defaultArgument =====
value: 10 hello 11.1
value: 10 hihi~ 11.1
value: 10 happy 21.5

===== functionOverloading(1) =====
empty input argument

===== functionOverloading(2) =====
input arguments: 1 3.1
*/
