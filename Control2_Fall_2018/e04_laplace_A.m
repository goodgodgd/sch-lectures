clear; clc
% �ɺ��� ���� ����
syms t x z s
disp('�ɺ��� �ð��Լ�')
f=-t^2

disp('���ö� ��ȯ (�⺻ ���ö� ���� s)')
F=laplace(f)

disp('���ö� ���� ���� (z)')
F=laplace(f,z)

disp('�ɺ��� �ð��Լ� - ���� ���� (t, x)')
f=-t^2*x

disp('���ö� ��ȯ (�⺻ �ð����� t)')
F=laplace(f)

disp('�ð����� �����Ͽ� ���ö� ��ȯ (x)')
F=laplace(f,x,s)
