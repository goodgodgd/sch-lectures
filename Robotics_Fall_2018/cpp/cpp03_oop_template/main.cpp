#include <iostream>

using namespace std;

class Character
{
public:
    Character(std::string _name)
        : hp(50), name(_name)
    {}

    void getDamage(int damage)
    {
        hp -= damage;
        if(hp <= 0)
            std::cout << name << " died" << std::endl;
        else
            std::cout << name << " is damaged. HP=" << hp << std::endl;
    }

    int attack(Character* other)
    {
        std::cout << name << " attacks" << std::endl;
        effect();
        other->getDamage(20);
    }
protected:
    virtual void effect() = 0;
    int hp;
    std::string name;
};

class Warrior: public Character
{
public:
    Warrior(std::string _name) : Character(_name) {}
protected:
    virtual void effect()
    {
        std::cout << name << " swing a sword" << std::endl;
    }
};

class Wizard: public Character
{
public:
    Wizard(std::string _name) : Character(_name) {}
protected:
    virtual void effect()
    {
        std::cout << name << " shoot a fireball" << std::endl;
    }
};

int main()
{
    Character* warrior = new Warrior("warrior");
    Character* wizard = new Wizard("wizard");
    warrior->attack(wizard);
    wizard->attack(warrior);
    warrior->attack(wizard);
    warrior->attack(wizard);
    return 0;
}
// 객체 지향 개념
// 캡슐화: 객체의 속성(데이터)와 속성을 다루는 방법(함수)을 한데 묶음
//         객체의 상세한 내용을 외부에 숨기고 메시지(함수)만으로 객체와 상호작용
//         객체 내부의 hp, name은 밖에서 알 필요가 없으므로 숨기고 (private)
//         attack으로만 두 캐릭터가 상호작용한다.
// 추상화: 객체에서 공통된 속성과 행위를 추출하는 것
//         Warrior와 Wizard의 공통된 속성을 묶어 Character로 추상화하여
//         두 가지 객체를 Character의 두 객체로 표현한다.
// 상속:   부모 클래스의 특징(함수, 변수)을 자식 클래스에 물려주는 것
//         자식 클래스는 부모 클래스의 공개 멤버 변수와 함수를 쓸 수 있고
//         새로운 멤버 변수와 함수를 추가하여 기능을 확장할 수 있다.
// 다형성: 부모 클래스의 가상 함수를 자식클래스에서 재정의 할 수 있다.
//         상속 받은 함수의 이름은 그대로 두고 기능만 바꿀 수 있다.
