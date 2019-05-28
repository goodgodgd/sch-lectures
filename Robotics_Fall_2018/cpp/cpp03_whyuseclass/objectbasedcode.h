#ifndef OBJECTBASEDCODE_H
#define OBJECTBASEDCODE_H

#include <iostream>
#include <string>
using namespace std;

class Fruit
{
public:
    // 기본 생성자 정의
    // 멤버 변수를 고정된 기본 값으로 초기화
    Fruit()
    {
        name = "fruit";
        sweetness = 0;
        sweetIncr = 0.1f;
    }

    // 입력인자가 있는 생성자 정의
    // 멤버 변수를 입력인자로 초기화
    Fruit(string _name, float _sweetness, float _sweetIncr)
    {
        name = _name;
        sweetness = _sweetness;
        sweetIncr = _sweetIncr;
    }

    // 함수기반 코드와 달리 데이터가 내부에 있으므로 외부에서 많은 인자를 받을 필요 없음
    void ripen()
    {
        sweetness += sweetIncr;
        cout << name << "'s current sweetness=" << sweetness << endl;
    }

    bool isEatable()
    {
        cout << name << " is eatable? " << ((sweetness > 2.f) ? "yes" : "no") << endl;
        return (sweetness > 2.f);
    }

private:
    // 공통의 속성: 이름, 당도, 당도증가율 -> 멤버 변수
    string name;
    float sweetness;
    float sweetIncr;
};

// 객체 지향 개념(1)
// 추상화: 객체에서 공통된 속성과 행위를 추출하는 것
//         사과와 오렌지의 공통된 속성을 묶어 "과일"로 추상화하여
//         비슷한 두 객체를 "과일"의 두 객체로 표현한다.
// 캡슐화: 객체의 속성(데이터)와 속성을 다루는 방법(함수)을 한데 묶음
//         객체의 상세한 내용을 외부에 숨기고 메시지(함수)만으로 객체와 상호작용
//         외부에서 Fruit 객체를 쓰기 위해 이름, 당도, 무게를 알 필요가 없다.
//         그저 계속 익히면서 먹을수 있는지 확인만 하면 된다.

#endif // OBJECTBASEDCODE_H
