#include <cassert>
#include "matrix.h"
using std::cout;
using std::endl;

#define EXCEPTION_CASE(expression)                           \
    try                                                      \
    {                                                        \
        expression;                                          \
        assert(false && "This test MUST raise a exception"); \
    }                                                        \
    catch (MyException & e)                                  \
    {                                                        \
        cout << "exception: " << e.what() << endl;           \
    }

void test_create_matrices()
{
    cout << "==========\ntest_create_matrices\n";
    // explicitly assigned template type
    Matrix<int> m0({1, 2, 3, 4}, 2, 2);
    // Class template argument deduction (CTAD) (since C++17)
    // https://en.cppreference.com/w/cpp/language/class_template_argument_deduction
    Matrix m1({1, 2, 3, 4}, 2, 2);
    Matrix m2(1, 2, 2);
    cout << "m1\n"
         << m1;
    cout << "m2\n"
         << m2;
    Matrix m3 = m2;
    cout << "m3\n"
         << m3;
    EXCEPTION_CASE(Matrix m4({1, 2, 3, 4, 5}, 2, 2))
    EXCEPTION_CASE(Matrix m5({1, 2, 3}, 2, 3))
}

void test_access_element()
{
    cout << "==========\ntest_access_element\n";
    Matrix m1({1, 2, 3, 4}, 2, 2);
    cout << "elem at (1,0): " << m1(1, 0) << endl;
    cout << "elem at (0,1): " << m1(0, 1) << endl;
    m1(0, 0) = 10;
    cout << "revised elem at (0,0): " << m1(0, 0) << endl;
    EXCEPTION_CASE(m1(3, 0))
    EXCEPTION_CASE(m1(1, 2))
}

void test_add_matrices()
{
    cout << "==========\ntest_add_matrices\n";
    Matrix m1({1, 2, 3, 4}, 2, 2);
    Matrix m2({4, 3, 2, 1}, 2, 2);
    Matrix m3 = m1 + m2;
    cout << "m3\n"
         << m3;
    Matrix m4({1, 2, 3, 4, 5, 6}, 3, 2);
    Matrix m5({1, 2, 3, 4, 5, 6}, 2, 3);
    EXCEPTION_CASE(m1 + m4)
    EXCEPTION_CASE(m1 + m5)
}

int main()
{
    test_create_matrices();
    test_access_element();
    test_add_matrices();
    return 0;
}