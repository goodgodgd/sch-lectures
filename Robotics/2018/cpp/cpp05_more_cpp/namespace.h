#ifndef CPP_EXAMPLES_H
#define CPP_EXAMPLES_H

#include <iostream>
using namespace std;

namespace physics
{
    void whatIsRight()
    {
        cout << "physics: when facing north, east is right side" << endl;
    }
}

namespace morality
{
    void whatIsRight()
    {
        cout << "morality: correct and agreeing with facts" << endl;
    }
}

namespace law {
    void whatIsRight()
    {
        cout << "law: What you are legally entitled to do or have" << endl;
    }
}

// 복잡한 프로그램을 짜다보면 같은 이름을
// 다른 맥락에서 사용해야 할 때가 있다.
// 이름 중복을 피하기 위해 physics_whatIsRight() 처럼
// 이름에 직접 맥락을 추가하는 방식은 whatIsLeft_in_physics() 처럼
// 일관성 없는 이름이 나올수 있기 때문에
// 다른 사람이 코드를 이해하기 어렵다.

// 함수명을 길게 쓰는 것보다는 그런 공통의 맥락들을 모아서
// 하나의 namespace로 묶어주는 것이 좋다.
void practiceNamespace()
{
    cout << "===== namespace =====" << endl;
    physics::whatIsRight();
    morality::whatIsRight();
    law::whatIsRight();
}

#endif // CPP_EXAMPLES_H
