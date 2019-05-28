clear; clc
syms s a t x

disp('�ɺ��� ���ö� �Լ�')
F_s=(s^2+12)/(s^3+5*s^2+6*s);
pretty(F_s)

disp('���ö� ����ȯ')
f_t=ilaplace(F_s)

disp('�κкм� ����: �и�, ����, ������')
[num, den]=numden(F_s);
num=sym2poly(num);
den=sym2poly(den);
[r,p,k]=residue(num,den);
coef=r'
pole=p'
rema=k'

disp('���ö� ����ȯ: �⺻ �ð� ���� t, ���ö� ���� s')
F=1/(s-2*a)^2;
pretty(F)
f_t=ilaplace(F)

disp('�ð� ���� x �����Ͽ� ����ȯ')
f_x=ilaplace(F,x)

disp('�ð� ���� x, ���ö� ���� a �����Ͽ� ����ȯ')
f_x=ilaplace(F,a,x)
