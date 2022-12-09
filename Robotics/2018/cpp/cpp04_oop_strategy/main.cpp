#include <iostream>

class Weapon {
public:
    virtual void effect() = 0;
};

class FlamingSword: public Weapon {
public:
    virtual void effect() {
        std::cout << " swings a sword with a flaming effect" << std::endl;
    }
};

class FreezingSword: public Weapon {
public:
    virtual void effect() {
        std::cout << " swings a sword with frozen effect" << std::endl;
    }
};

class Character {
public:
    Character(std::string _name)
        : hp(50), name(_name)
    {}

    void setWeapon(Weapon* _weapon) {
        weapon = _weapon;
    }
    void getDamage(int damage) {
        hp -= damage;
        if(hp <= 0)
            std::cout << name << " died" << std::endl;
        else
            std::cout << name << " is damaged. HP=" << hp << std::endl;
    }
    int attack(Character* other) {
        std::cout << name << " attacks" << std::endl;
        effect();
        other->getDamage(20);
    }
protected:
    virtual void effect() = 0;
    Weapon* weapon;
    int hp;
    std::string name;
};

class Warrior: public Character
{
public:
    Warrior(std::string _name) : Character(_name) {}
protected:
    virtual void effect() {
        std::cout << name;
        weapon->effect();
    }
};

int main()
{
    Character* david = new Warrior("david");
    Character* hans = new Warrior("hans");
    std::cout << "david equipped a flaming sword" << std::endl;
    david->setWeapon(new FlamingSword);
    david->attack(hans);
    std::cout << "david changed a weapon to a freezing sword" << std::endl;
    david->setWeapon(new FreezingSword);
    david->attack(hans);
    return 0;
}
// 템플릿 패턴: 여러 단계로 이루어진 알고리즘에서 일부 단계만 자식 클래스에서 변형하여 사용
//			알고리즘의 전체 구조가 정해진 상태에서 일부 루틴을 다르게 구현한 객체들이 필요할 때 사용
// 전략 패턴: 같은 기능을 하지만 다르게 구현된 알고리즘을 캡슐화 (클래스로 객체화)하여
//			알고리즘을 run time에서 교체가능하게 만든다.
//			알고리즘을 사용하는 client (Character)와는 독립적으로 알고리즘을 변경할 수 있다.
//			예를 들어 속도가 빠른 대신 메모리를 많이 사용하는 알고리즘과 
//			반대 알고리즘을 필요에 따라 교환할 수 있다.
