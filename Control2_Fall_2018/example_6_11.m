clc; clear

Mp = 0.2;
v1 = log(Mp);
zeta = sqrt(v1^2/(pi^2+v1^2));
fprintf('최대초과 조건으로부터 zeta = %f\n\n', zeta)
izeta = sqrt(1-zeta^2);
wn = 11.87;
p1 = [-zeta*wn, izeta*wn];
fprintf('PD 보상전 최대초과를 만족하는 근의 위치 p1 = %.4f + j%.4f\n\n', p1(1), p1(2))

s = tf('s');
G1 = (s+8)/((s+3)*(s+6)*(s+10));
figure(1)
plot(p1(1),p1(2), '*k')
hold on
rlocus(G1)
axis([-50 2 -25 25])
set(gcf,'Position',[100 500 600 600])
hold off

p2 = 2*p1;
fprintf('상승시간을 반으로 줄이는 근의 위치 p2 = %.4f + j%.4f\n\n', p2(1), p2(2))
theta_z1 = atan2(p2(2),8+p2(1));
theta_p1 = atan2(p2(2),3+p2(1));
theta_p2 = atan2(p2(2),6+p2(1));
theta_p3 = atan2(p2(2),10+p2(1));
ang_G = theta_z1 - theta_p1 - theta_p2 - theta_p3;
fprintf('s=p2 일 때, G(s)의 위상 = theta_z1 - theta_p1 - theta_p2 - theta_p3\n')
fprintf('= %.3f - (%.3f) - (%.3f) - (%.3f) = %f \n\n', theta_z1, theta_p1, theta_p2, theta_p3, ang_G)
ang_zc = -pi - ang_G;
zc = p2(2)/tan(ang_zc)-p2(1);
fprintf('PD 제어기의 위상 = %f, 영점의 위치 = %f\n', rad2deg(ang_zc), zc)

s = tf('s');
C = (s+zc)*(s+0.6)/s
disp('PID 보상된 시스템의 개로전달함수')
G2 = C*G1
figure(2)
plot(p2(1), p2(2), '*k')
hold on
rlocus(G2)
axis([-100 2 -50 50])
set(gcf,'Position',[800 500 600 600])
hold off
