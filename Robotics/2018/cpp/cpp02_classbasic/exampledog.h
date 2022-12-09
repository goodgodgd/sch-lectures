#ifndef EXAMPLEDOG_H
#define EXAMPLEDOG_H

#include <iostream>     // cout 활용
#include <string>       // string 활용

// .h 파일에서는 class 선언 내부에서 함수와 변수를 선언한다.

class ExampleDog
{
// 공개 영역
public:
    // 생성자: 클래스 객체 생성시 실행되는 함수, 클래스와 같은 이름으로 선언
    // 입력 인자는 있을 수 있으나 리턴 타입은 없다.
    // 기본 생성자 선언
    ExampleDog();

    // 인자가 있는 생성자 선언
    ExampleDog(std::string _name, int _age);

    // 소멸자: 클래스 객체 파괴(메모리 해제)시 실행되는 함수, ~[클래스 이름]으로 선언
    // 입력 인자도 없고 리턴 타입도 없다.
    // 소멸자 선언
    ~ExampleDog();

    // 공개 멤버 함수: 외부에서 호출 가능
    void grow();
    void bark();
    // 비공개 변수의 확인은 공개 함수로 한다.
    int getAge();

    // 공개 변수가 있을 수 있으나 권장하지 않음


// 비공개 영역
private:
    // 비공개 멤버 함수: 외부에서 호출 불가, 내부적으로만 사용 가능
    void increaseAge();

    // 비공개 멤버 변수: 일반적으로 클래스 변수는 private 으로 숨긴다.
    std::string name;
    int age;
};

#endif // EXAMPLEDOG_H
