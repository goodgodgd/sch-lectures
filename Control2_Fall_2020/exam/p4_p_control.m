clc; clear

% 문제 정의
s = tf('s');
otf = 1/((s+1)*(s+5))
% 최대초과 비율
os = 0.15;

% 근궤적 그리기
figure(1)
rlocus(otf)
hold on

% 점근선과 실수축의 교차점 계산
poles = pole(otf);
zeros = zero(otf);
disp(poles')
num_asym = size(poles,1) - size(zeros,1);
fprintf('발산하는 점근선의 개수: %d\n', num_asym)
asym_point = (sum(poles) - sum(zeros))/(num_asym);
fprintf('점근선과 실수축이 만나는 점: %.1f\n', asym_point)

% 목표 극점의 실수부
pole_real = asym_point;
fprintf('분기점=점근선 교차점 일때, 극점의 실수부 real(p) = %.1f\n', pole_real)
% 목표 극점의 허수 범위 구하기
[zeta, theta] = draw_overshoot_line(os, 'r--');
pole_imag = abs(pole_real * tan(theta));
fprintf('조건을 만족하는 극점의 위치 = %.4f + j%.4f\n', pole_real, pole_imag)
% 목표 극점 그리기
plot(pole_real, pole_imag, 'rd')
target_pole = pole_real + 1i*pole_imag;

% target pole을 지날때 K값 구하기
K = find_K(otf, target_pole);
fprintf('목표 극점에서의 K 값: %.4f\n', K)

hold off
axis([-12 2 -7 7])
set(gcf,'Position',[200 200 400 400])


function [zeta, theta] = draw_overshoot_line(os, style)
    zeta = sqrt(log(os)^2 / (log(os)^2 + pi^2));
    theta = acos(zeta);
    fprintf('%%OS=%.2f, zeta=%.4f, theta=%.3f(deg)\n', os, zeta, rad2deg(theta))
    plot([0 -100*cos(theta)], [0  100*sin(theta)], style)
    plot([0 -100*cos(theta)], [0 -100*sin(theta)], style)
end

function K = find_K(otf, pole_pos)
    [num, den] = tfdata(otf);
    num = num{1};
    den = den{1};
    syms w
    K_w = -poly2sym(den, w) / poly2sym(num, w);
    K = double(subs(K_w, w, pole_pos));
end