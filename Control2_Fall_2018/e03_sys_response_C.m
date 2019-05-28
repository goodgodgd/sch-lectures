clc; clear
% 시스템 전달함수 정의
s=tf('s') ;                                     
G_s=4*(s+2)/(s*(s+3)*(s+7))
% 단위 귀환 시스템의 전달함수
sys=feedback(G_s,1)

% 단위 램프 응답 계산 t=시간, u=입력, y=출력
t=0:0.1:100;
u=t;
[y,t]=lsim(sys,u,t);

% 입력(u)과 출력(y) 그리기
plot(t,u,'r-', t,y,'b-')
xlabel('Time(sec)')
ylabel('Amplitude')
title('Unity Feedback System: Ramp function')
grid
