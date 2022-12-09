#include "functionbasedcode.h"
#include "objectbasedcode.h"

void functionBasedCode()
{
    cout << endl << "==== Function based code =====" << endl;
    float appleSweetness = 1.f;
    float orangeSweetness = 0.5f;

    while(!isEatable("apple", appleSweetness))
        appleSweetness = ripenApple(appleSweetness);

    while(!isEatable("orange", orangeSweetness))
        orangeSweetness = ripenOrange(orangeSweetness);
}

void objectBasedCode()
{
    cout << endl << "==== Object based code =====" << endl;
    // 객체를 사용하여 변수 선언이 줄어들고 변수의 이름이 간단해진다.
    Fruit apple("apple", 1.f, 0.3f);
    Fruit orange("orange", 0.5f, 0.5f);

    // 함수 호출 인자도 줄었다.
    while(!apple.isEatable())
        apple.ripen();

    while(!orange.isEatable())
        orange.ripen();
}

// 클래스 사용의 장점
// 1) 편의성 = 관리의 용이성 = 응집성
//  비슷한 속성과 기능을 클래스안에 묶어놓았기 때문에
//  코드 작성과 수정, 확장이 편리하다.
//  객체추가: apple, orange 외에 banana를 추가할 때
//      bananaSweetness, ripenBanana() 를 따로 선언할 필요없다
//  기능추가: isEatable()에 당도 외에 무게라는 속성이 필요하게 되면
//      함수기반 코드는 appleWeight, orangeWeight ... 등을 따로 선언하고
//      ripenApple(), ripenOrange()에 무게 인자를 각각 추가해야 한다.
//      객체기반 코드는 Fruit 이라는 클래스에서 한번씩만 수정하면 된다.
//  객체지향뿐만 아니라 모든 좋은 코드는 같은 패턴의 코드가 반복되는
//  '중복'을 지양한다.
//  객체지향의 모든 패턴들은 코드 중복을 없애고 비슷한 기능과 속성을
//  한 곳으로 '응집'시킨다.
// 2) 가독성
//  좋은 코드는 신문을 읽듯이 문장처럼 읽혀야 한다.
//  그런데 단어가 너무 길면 읽기 어렵다.
//  func_object() 식의 이름 보다는 object.func() 이 잘 읽히고
//  코드가 많고 복잡해지면 func_object() 식의 이름은
//  중복을 피하기 위해 점점 길어질 수 밖에 없다.
//      e.g. weight_chicken() -> weight_animal_chicken(), weight_food_chicken()
//  object.func() 식의 이름은 class name에 유형이 드러나기 때문에
//  함수나 변수명을 길게 짓지 않아도 의미가 명확하다.


int main()
{
    // 동작은 같지만 구현 방법이 전혀 다른 두 함수
    functionBasedCode();

    objectBasedCode();
}


/* Program output

==== Function based code =====
apple is eatable? no
apple's current sweetness=1.3
apple is eatable? no
apple's current sweetness=1.6
apple is eatable? no
apple's current sweetness=1.9
apple is eatable? no
apple's current sweetness=2.2
apple is eatable? yes
orange is eatable? no
orange's current sweetness=1
orange is eatable? no
orange's current sweetness=1.5
orange is eatable? no
orange's current sweetness=2
orange is eatable? no
orange's current sweetness=2.5
orange is eatable? yes

==== Object based code =====
apple is eatable? no
apple's current sweetness=1.3
apple is eatable? no
apple's current sweetness=1.6
apple is eatable? no
apple's current sweetness=1.9
apple is eatable? no
apple's current sweetness=2.2
apple is eatable? yes
orange is eatable? no
orange's current sweetness=1
orange is eatable? no
orange's current sweetness=1.5
orange is eatable? no
orange's current sweetness=2
orange is eatable? no
orange's current sweetness=2.5
orange is eatable? yes

*/
