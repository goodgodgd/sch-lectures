clc; clear
% 시스템 전달함수 정의
s=tf('s');
G_s=4*(s+2)/(s*(s+3)*(s+7))

% 단위 귀환 시스템의 전달함수
sys=feedback(G_s,1)

% 단위 계단 응답 계산 y=출력, t=시간
[y,t]=step(sys);

% 입력데이터 만들기: 출력시간의 길이만큼 1의 배열 생성
u=ones(size(t));

% 입력(u)과 출력(y) 그리기
plot(t,u,'r-', t,y,'b-')
axis([0 15 0 1.1])
xlabel('Time(sec)')
ylabel('Amplitude')
title('Unity Feedback System: Step function')
grid
