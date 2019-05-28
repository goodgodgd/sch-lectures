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
