#ifndef CONSTSTATIC_H
#define CONSTSTATIC_H

#include <iostream>
using namespace std;

void count()
{
    // 함수 내부에 선언된 static 변수는 함수가 끝나도 소멸되지 않고
    // 함수 내부에서 변경된 값은 다음 호출시 그대로 유지된다.
    // 특정 함수 내부에서만 사용되는 변수는 static으로 선언하는 것이
    // 안전하다.
    // 외부에서 선언할 시, 다른 함수에서 의도하지 않은 방법으로
    // 변수를 사용하거나 수정할 수 있다.
    static int value=0;
    cout << "count: " << ++value << endl;
}

class Student
{
public:
    Student(int _score)
    {
        score = _score;
        // static 멤버 함수/변수는 일반적인 멤버 함수에서 접근가능하다.
        cout << ++n_students << "'th Student is created." << endl;
    }

    void study()
    {
        score++;
    }

    void setScore(const int _score)
    {
        score = _score;
    }

    // 클래스 객체를 const로 선언한 경우 멤버 함수를 사용할 수 없다.
    // 하지만 내부 속성을 건드리지 않는 함수는 함수 선언 끝에 const를 붙이면
    // const 객체에서도 호출할 수 있다.
    int getScore() const
    {
        return score;
    }

    static void numberOfStudents()
    {
        // static 멤버 함수에서는 static 멤버 변수만 접근할 수 있다.
        cout << "Number of students: " << n_students << endl;
        // static 함수에서는 일반 멤버 함수/변수에 접근할 수 없다.
    }

private:
    static int n_students;
    int score;
};

int Student::n_students = 0;


// reference 인자의 장점: 객체를 복사하지 않고 포인터만 넘겨서
// 함수 호출이 가벼워진다.
void studyHard(Student& a)
{
    a.study();
    a.study();
}

// 대신 입력 인자를 reference로 넘기면 원치 않게
// 클래스의 속성이 밖에서도 변경될 수 있으므로
// const 키워드와 함께 주면 함수에서는 속성을 변경시킬 수 없다.
void printScore(const Student& a)
{
    cout << "score = " << a.getScore() << endl;
    // 내부 속성을 변경하는 study() 함수를 부르면 문법 에러
//    a.study();
}


void practiceConstStatic()
{
    cout << endl << "===== static/const =====" << endl;
    count();
    count();
    count();

    // 학생 객체 생성
    Student kim(78);
    Student* lee = new Student(90);

    // 일반 함수는 객체를 통해서만 호출 가능하다.
    cout << "kim's score is " << kim.getScore() << endl;
    kim.setScore(85);
    cout << "kim's score is updated to " << kim.getScore() << endl;
    cout << "lee's score is " << lee->getScore() << endl;

    // const 객체는 const 함수만 부를 수 있다.
    const Student park(60);
    cout << "const park's score: " << park.getScore() << endl;
//    cout << "const park's score: " << park.setScore(50) << endl;

    // static 멤버 함수는 클래스에서 직접 부를 수도 있고 객체에서 부를수도 있다.
    Student::numberOfStudents();
    kim.numberOfStudents();
    lee->numberOfStudents();

    // reference로 들어간 입력인자는 내부 속성이 변경될 수 있다.
    studyHard(kim);
    // const reference로 들어간 입력인자는 내부 속성이 변경될 수 없다.
    printScore(kim);
}


#endif // CONSTSTATIC_H
