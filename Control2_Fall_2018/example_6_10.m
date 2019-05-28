clc; clear
disp('���� 6-10 PD ����� ����')
s = tf('s');
G1 = 1/(s*(s+4)*(s+6));

% root locus �׸���
figure(1)
rlocus(G1)
axis([-12 2 -7 7])
set(gcf,'Position',[100 500 600 600])   % ũ�� ��ġ����
hold on

disp('�ִ��ʰ� �������κ��� zeta ���')
Mp = 0.16;
v1 = log(Mp);
zeta_Mp = sqrt(v1^2/(pi^2+v1^2))
disp('������ �����ϴ� zeta�� ����')
zeta = 0.504
theta = asin(zeta);
plot([0 -100*sin(theta)], [0  100*cos(theta)], 'c--')
plot([0 -100*sin(theta)], [0 -100*cos(theta)], 'c--')

disp('�ٱ������� Mp ������ �����ϴ� ���� ����')
p1 = [-1.205, 2.064]
plot(p1(1), p1(2), '*k')

disp('�����ð��� 1/3�� ���̴� ���� ����')
p2 = p1*3
plot(p2(1), p2(2), '*r')
hold off

disp('�������ǿ� ���� ������ ���� ���')
ang_G1 = -atan2(p2(2), p2(1)) - atan2(p2(2), p2(1)+4) - atan2(p2(2), p2(1)+6);
fprintf('G(s)�� ���� = -theta_p1 - theta_p2 - theta_p3 = -(%.3f) - (%.3f) - (%.3f) = %f\n', ...
    -atan2(p2(2), p2(1)), -atan2(p2(2), p2(1)+4), -atan2(p2(2), p2(1)+6), ang_G1)
% theta_z + ang_G1 = -180
theta_z = -pi - ang_G1;
fprintf('PD ������� ���� = %f\n', rad2deg(theta_z))
zero = p2(2)/tan(theta_z) - p2(1);
fprintf('������ ��ġ = %f\n', zero)

disp('PD����Ⱑ ����� ���������Լ�')
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
fprintf('��ǥ�ϴ� ���� p2�� ������ K = %f\n', K)

