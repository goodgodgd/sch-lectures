#include "exampledog.h"

int main()
{
    // 기본 클래스 사용법
    std::cout << "===== Learn class usage =====" << std::endl;
    // 클래스 객체 선언
    {
        ExampleDog dog;
        dog.grow();
        dog.bark();
        dog.grow();
        dog.bark();
    }

    // new를 이용한 클래스 객체 선언 (인자 입력)
    ExampleDog* poodle = new ExampleDog("poodle", 3);
    poodle->grow();
    poodle->bark();
    poodle->grow();
    poodle->bark();
    // delete를 이용한 객체 소멸
    delete poodle;

    return 0;
}

/* Program output

===== Learn class usage =====
dog(0) is created
dog grows
dog(1): wal wal!!
dog grows
dog(2): wal wal!!
poodle(3) is created
poodle grows
poodle(4): wal wal!!
poodle grows
poodle(5): wal wal!!
poodle is destroyed
dog is destroyed
*/
