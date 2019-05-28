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
