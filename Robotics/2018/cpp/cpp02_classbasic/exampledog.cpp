#include "exampledog.h"


// .cpp 파일에서는 함수의 구현을 정의한다.

// 기본 생성자 정의
ExampleDog::ExampleDog()
{
    // 기본 생성자에서는 멤버 변수를 초기화 시켜주는 것이 좋다.
    name = "dog";
    age = 0;
    std::cout << name << "(" << age << ") is created" << std::endl;
}

// 인자가 있는 생성자 정의
ExampleDog::ExampleDog(std::string _name, int _age)
{
    name = _name;
    age = _age;
    std::cout << name << "(" << age << ") is created" << std::endl;
}

// 소멸자 정의
ExampleDog::~ExampleDog()
{
    std::cout << name << " is destroyed" << std::endl;
}

// 공개 멤버 함수 정의
void ExampleDog::grow()
{
    // 복잡한 알고리즘의 경우 공개함수에서 바로 구현하기 보다는
    // 비공개 함수에서 구체적인 구현을 하는 것이 좋다.
    // grow(): 클래스 사용자를 위한 함수 이름
    // increaseAge(): 실제 구현 방법을 나타낸 함수 이름
    std::cout << name << " grows" << std::endl;
    increaseAge();
}

void ExampleDog::bark()
{
    std::cout << name << "(" << age << "): wal wal!!" << std::endl;
}

int ExampleDog::getAge()
{
    return age;
}

// 비공개 멤버 함수 정의
void ExampleDog::increaseAge()
{
    age++;
}
