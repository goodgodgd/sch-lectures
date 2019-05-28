clc; clear

%% given system and performance conditions
disp('system with 3 poles and 1 zero')
s = tf('s');
G_s = (s+3)/((s+7)*(s^2+2*s+2));

figure(1)
rlocus(G_s)
axis([-10 2 -6 6])
set(gcf,'Position',[100 100 600 600])

tr =1.5;    % 상승시간 1초 이하
Mp = 0.2;   % overshoot 20% 이하
ts = 3.5;   % 정착시간 3초 이하

%% designing controller
% 2.4/wn < tr  ->  wn > 2.4/tr
wn_tr = 2.4/tr
% exp(-zeta*pi / sqrt(1-zeta^2)) < Mp
% ->  zeta^2 > (lnM)^2 / ((lnM)^2 + pi^2)
zeta_Mp = sqrt(log(Mp)^2 / (log(Mp)^2 + pi^2))
theta_Mp = asin(zeta_Mp)
% 4/sig < ts  ->  sig > 4/ts
sig_ts = 4/ts

% circle with radius wn_tr
a = 0:0.01:2*pi;
x = wn_tr*cos(a);
y = wn_tr*sin(a);
hold on
plot(x, y, 'm--')

% line with angle theta_Mp from imaginary axis
plot([0 -100*sin(theta_Mp)], [0  100*cos(theta_Mp)], 'c--')
plot([0 -100*sin(theta_Mp)], [0 -100*cos(theta_Mp)], 'c--')

% line s=-sig
plot([-sig_ts, -sig_ts], [-100, 100], 'k--')
hold off

%% check step response
% select K
K = 10;
% transfer function of feedback system
T_s = feedback(K*G_s, 1)
%          10 s + 30
%   -----------------------
%   s^3 + 9 s^2 + 26 s + 44

% compensate DC gain to 1
T_s = T_s/30*44
[y, t] = step(T_s);
u=ones(size(t));

figure(2)
plot(t,u,'r-', t,y,'b-')
axis([0 5 0 1.5])
hold on

% draw performance conditions
plot([tr, tr], [-10, 10], 'm--')    % rise time
plot([0, 10], [1+Mp, 1+Mp], 'c--')  % overshoot
plot([0, 10], [0.98, 0.98], 'k--')  % settling time
plot([0, 10], [1.02, 1.02], 'k--')  % settling time
plot([ts, ts], [-10, 10], 'k--')  % settling time
