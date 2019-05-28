### 1. 라플라스 변환
```
clear; clc
% 심볼릭 변수 생성
syms t x z s
disp('심볼릭 시간함수')
f=-t^2

disp('라플라스 변환 (기본 라플라스 변수 s)')
F=laplace(f)

disp('라플라스 변수 지정 (z)')
F=laplace(f,z)

disp('심볼릭 시간함수 - 다중 변수 (t, x)')
f=-t^2*x

disp('라플라스 변환 (기본 시간변수 t)')
F=laplace(f)

disp('시간변수 지정하여 라플라스 변환 (x)')
F=laplace(f,x,s)
```


### 2. 라플라스 역변환
```
clear; clc
syms s a t x

disp('심볼릭 라플라스 함수')
F_s=(s^2+12)/(s^3+5*s^2+6*s);
pretty(F_s)

disp('라플라스 역변환')
f_t=ilaplace(F_s)

disp('부분분수 전개: 분자, 극점, 나머지')
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
```
