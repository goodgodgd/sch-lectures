clc; clear; close all
% system with 3 poles and 1 zero
s = tf('s');
sys = (s+3)/((s+7)*(s^2+2*s+2));

% figure(1)
rlocus(sys)
hold on
axis([-10 2 -6 6])
% set(gcf,'Position',[100 100 800 800])

tp = 1.5;   % 첨두시간 1.5초 이하
Mp = 0.2;   % overshoot 20% 이하
ts = 3.5;   % 정착시간 3.5초 이하

% pi/wd < tp  ->  wd > pi/tp
wd_tp = 2.4/tp
% exp(-zeta*pi / sqrt(1-zeta^2)) < Mp
% ->  zeta^2 > (lnM)^2 / ((lnM)^2 + pi^2)
zeta_Mp = abs(log(Mp) / sqrt(log(Mp)^2 + pi^2))
theta_Mp = asin(zeta_Mp)
% 4/sig < ts  ->  sig > 4/ts
sig_ts = 4/ts
% line s=jwd_tp
plot([-100, 100], [wd_tp, wd_tp], 'm--')
plot([-100, 100], [-wd_tp, -wd_tp], 'm--')

% line with angle theta_Mp from imaginary axis
plot([0 -100*sin(theta_Mp)], [0  100*cos(theta_Mp)], 'c--')
plot([0 -100*sin(theta_Mp)], [0 -100*cos(theta_Mp)], 'c--')

% line s=-sig_ts
plot([-sig_ts, -sig_ts], [-100, 100], 'k--')
hold off
