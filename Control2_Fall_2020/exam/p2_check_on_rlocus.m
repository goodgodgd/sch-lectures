clc; clear

s = tf('s');
G = ((s+2)^2 + 4) / ((s+1)^2 + 4) / ((s+3)^2 + 4);

% 1-1  축 그리기
draw_axis([-6 2 -4 4])
hold on
% 확인할 점
plot([-2], [1], 'rd')
% 극점 영점
plot(real(pole(G)), imag(pole(G)), 'xk')
plot(real(zero(G)), imag(zero(G)), 'ok')
hold off 
pause

% 1-2  축 그리기
draw_axis([-6 2 -4 4])
hold on
% 확인할 점
plot([-2], [3], 'rd')
% 극점 영점
plot(real(pole(G)), imag(pole(G)), 'xk')
plot(real(zero(G)), imag(zero(G)), 'ok')
hold off
pause


G = 3 / ((s+1)*(s+1+1/sqrt(3))*(s+1+sqrt(3)));

% 2-1  축 그리기
draw_axis([-4 1 -3 3])
hold on
% 확인할 점
plot([-1], [1], 'rd')
% 극점 영점
plot(real(pole(G)), imag(pole(G)), 'xk')
plot(real(zero(G)), imag(zero(G)), 'ok')
hold off
pause

% 2-2  축 그리기
draw_axis([-4 1 -3  3])
hold on 
% 확인할 점
plot([0], [2], 'rd')
% 극점 영점
plot(real(pole(G)), imag(pole(G)), 'xk')
plot(real(zero(G)), imag(zero(G)), 'ok')
hold off
pause

% 근궤적 위의 점 확인
rlocus(G)
hold on
% 확인할 점
plot([-1 0], [1 2], 'rd')
% 극점 영점
plot(real(pole(G)), imag(pole(G)), 'xk')
plot(real(zero(G)), imag(zero(G)), 'ok')
hold off
axis([-4 1 -3  3])
pause


function draw_axis(range)
    % 축 그리기
    plot([0 0], [-100 100], '-k')
    hold on
    plot([-100 100], [0 0], '-k')
    % 위치 고정
    hold off
    axis(range)
    set(gcf,'Position',[200 200 400 350])
end