#include <iostream>
#include <string>


class Phone
{
public:
    Phone()
    {
        std::cout << "phone instance is created" << std::endl;
    }

    bool text(std::string receiverNumber, std::string msg)
    {
        if(doesReceiverExist(receiverNumber)==false)
            return false;
        sendMsg(msg);
        return checkReceived();
    }

    bool doesReceiverExist(std::string receiverNumber) { return true; }
    bool checkReceived() { return true; }
    virtual void sendMsg(std::string msg)
    {
        std::cout << "send msg " << msg << " by [text app]" << std::endl;
    }
};

// 객체 지향 개념(2)
// 상속: 부모 클래스의 특징(함수, 변수)을 자식 클래스에 물려주는 것
//      자식 클래스는 부모 클래스의 공개 멤버 변수와 함수를 쓸 수 있고
//      새로운 멤버 변수와 함수를 추가하여 기능을 확장할 수 있다.
// 다형성: 부모 클래스의 가상 함수를 자식클래스에서 재정의 할 수 있다.
//      상속 받은 함수의 이름은 그대로 두고 기능만 바꿀 수 있다.

class iPhone: public Phone
{
public:
    // 자식을 생성할 때 부모의 생성자가 실행된 뒤 자식의 생성자가 실행된다.
    iPhone()
    {
        std::cout << "apple iphone instance is created" << std::endl;
    }

    // 메소드 오버라이딩: 다형성을 구현하는 객체지향 언어의 기능
    // method: 함수
    // overriding: 존재하는 함수를 프로토타입이 같은 다른 함수로 대체
    virtual void sendMsg(std::string msg)
    {
        std::cout << "send msg " << msg << " by [iMessage]" << std::endl;
    }
};

class Galaxy: public Phone
{
public:
    // 자식을 생성할 때 부모의 생성자가 실행된 뒤 자식의 생성자가 실행된다.
    Galaxy()
    {
        std::cout << "ss galaxy instance is created" << std::endl;
    }

    // 메소드 오버라이딩
    virtual void sendMsg(std::string msg)
    {
        std::cout << "send msg " << msg << " by [kaTalk]" << std::endl;
    }
};

int main()
{

    // 클래스의 다형성을 보기 위해서는 반드시 포인터로 선언해야 한다.
    // 자식 클래스의 포인터는 부모 클래스의 포인터로 지정(assign)이 가능하다.
    // 부모 클래스의 포인터는 자식 클래스의 포인터로 지정 불가하다.
    std::cout << "===== create instances =====" << std::endl;
    Phone* phones[3];
    phones[0] = new Phone;
    phones[1] = new iPhone;
    phones[2] = new Galaxy;

    // phones[0], [1], [2] 모두 Phone 클래스로 선언이 되어 있지만
    // [1], [2]에서는 자식 클래스인 iPhone과 Galaxy의 text() 함수가 실행된다.
    std::cout << std::endl << "===== send text =====" << std::endl;
    phones[0]->text("010xxxxyyyy", "Hello out there!");
    phones[1]->text("010xxxxyyyy", "C++ supports OOP.");
    phones[2]->text("010xxxxyyyy", "OOP means object-oriented programming.");

    // 클래스에 가상함수(virtual)가 있는 경우
    // 추상 클래스(abstract class)라 부른다.
    // 추상 클래스 객체에서 함수를 부를 때
    // 객체가 선언된 타입에서 바로 부르지 않고
    // 이 객체의 실질 타입을 동적으로 찾아서 실질 타입의 함수를 부른다.
    // phones[2]->text() 함수를 부르면 Phone 클래스가 아닌
    // Galaxy 클래스의 text() 함수를 부르게 된다.

    // 추상 클래스의 포인터에 할당된 객체 타입은 동적으로 변할 수 있다.
    std::cout << std::endl << "===== change instance and send text =====" << std::endl;
    phones[0] = new Galaxy;
    phones[0]->text("010xxxxyyyy", "Hello out there!");
    phones[1]->text("010xxxxyyyy", "C++ supports OOP.");
    phones[2]->text("010xxxxyyyy", "OOP means object-oriented programming.");

    return 0;
}

/* Program output

===== create instances =====
phone instance is created
phone instance is created
apple iphone instance is created
phone instance is created
ss galaxy instance is created

===== send text =====
send msg Hello out there! by [text app]
send msg C++ supports OOP. by [iMessage]
send msg OOP means object-oriented programming. by [kaTalk]

===== change instance and send text =====
phone instance is created
ss galaxy instance is created
send msg Hello out there! by [kaTalk]
send msg C++ supports OOP. by [iMessage]
send msg OOP means object-oriented programming. by [kaTalk]
*/
