clc; clear
disp('예제 6-10 PD 제어기 설계')
s = tf('s');
G1 = 1/(s*(s+4)*(s+6));

% root locus 그리기
figure(1)
rlocus(G1)
axis([-12 2 -7 7])
set(gcf,'Position',[100 500 600 600])   % 크기 위치고정
hold on

disp('최대초과 조건으로부터 zeta 계산')
Mp = 0.16;
v1 = log(Mp);
zeta_Mp = sqrt(v1^2/(pi^2+v1^2))
disp('조건을 만족하는 zeta를 선택')
zeta = 0.504
theta = asin(zeta);
plot([0 -100*sin(theta)], [0  100*cos(theta)], 'c--')
plot([0 -100*sin(theta)], [0 -100*cos(theta)], 'c--')

disp('근궤적에서 Mp 조건을 만족하는 극점 선택')
p1 = [-1.205, 2.064]
plot(p1(1), p1(2), '*k')

disp('정착시간을 1/3로 줄이는 극점 설계')
p2 = p1*3
plot(p2(1), p2(2), '*r')
hold off

disp('위상조건에 의한 영점의 위상 계산')
ang_G1 = -atan2(p2(2), p2(1)) - atan2(p2(2), p2(1)+4) - atan2(p2(2), p2(1)+6);
fprintf('G(s)의 위상 = -theta_p1 - theta_p2 - theta_p3 = -(%.3f) - (%.3f) - (%.3f) = %f\n', ...
    -atan2(p2(2), p2(1)), -atan2(p2(2), p2(1)+4), -atan2(p2(2), p2(1)+6), ang_G1)
% theta_z + ang_G1 = -180
theta_z = -pi - ang_G1;
fprintf('PD 제어기의 위상 = %f\n', rad2deg(theta_z))
zero = p2(2)/tan(theta_z) - p2(1);
fprintf('영점의 위치 = %f\n', zero)

disp('PD제어기가 적용된 개로전달함수')
G2 = (s+zero)*G1
figure(2)
rlocus(G2)
axis([-12 2 -7 7])
set(gcf,'Position',[800 500 600 600])
hold on
plot(p2(1), p2(2), '*r')
plot([0 -100*sin(theta)], [0  100*cos(theta)], 'c--')
plot([0 -100*sin(theta)], [0 -100*cos(theta)], 'c--')
hold off

K = sqrt(p2(1)^2 + p2(2)^2) * sqrt((4+p2(1))^2 + p2(2)^2) ...
    * sqrt((6+p2(1))^2 + p2(2)^2) / sqrt((zero+p2(1))^2 + p2(2)^2);
fprintf('목표하는 극점 p2를 지나는 K = %f\n', K)

