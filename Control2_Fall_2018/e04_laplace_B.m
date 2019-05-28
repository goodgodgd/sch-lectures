clear; clc
syms s a t x

disp('심볼릭 라플라스 함수')
F_s=(s^2+12)/(s^3+5*s^2+6*s);
pretty(F_s)

disp('라플라스 역변환')
f_t=ilaplace(F_s)

disp('부분분수 전개: 분모, 극점, 나머지')
[num, den]=numden(F_s);
num=sym2poly(num);
den=sym2poly(den);
[r,p,k]=residue(num,den);
coef=r'
pole=p'
rema=k'

disp('라플라스 역변환: 기본 시간 변수 t, 라플라스 변수 s')
F=1/(s-2*a)^2;
pretty(F)
f_t=ilaplace(F)

disp('시간 변수 x 지정하여 역변환')
f_x=ilaplace(F,x)

disp('시간 변수 x, 라플라스 변수 a 지정하여 역변환')
f_x=ilaplace(F,a,x)
