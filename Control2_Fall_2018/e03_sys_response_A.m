clc; clear
% 전달함수 식의 계수로 전달함수 객체 생성
T = tf([1 4], [1 3 2])

% 전달함수 수식 입력
s = tf('s')
G = (s+1)/(s^2+3*s+2)

% 피드백 시스템의 전달함수
% H: feedback gain
H = 4;
F = feedback(G, H)
