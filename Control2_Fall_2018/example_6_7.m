clc; clear

s = tf('s');
G1 = (s+2)/(s^2+6*s+10);
H = 1/(s+1);
% T(s) = G(s)/(1 + K*G1(s)*H(s)) �̹Ƿ�
% 1 + K*G1(s)*H(s) = 0 �� �Ǵ� �ٵ��� �ٱ����� �̷��.
disp('�� �ý����� ���������Լ�')
G2 = G1*H

% ���� �ٱ����� �׷����� �ٱ����� �����غ���
figure(1)
rlocus(G2)
axis([-5 1 -5 5])
hold on

disp('1. G2�� ���� ���� ���ϱ�')
poles = pole(G2)
zeros = zero(G2)
pause

disp('2. �ٱ����� ���ټ� ���ϱ�')
num_asym = size(poles,1) - size(zeros,1);
fprintf('�߻��ϴ� ���ټ��� ����: %d\n', num_asym)
asym_point = (sum(poles) - sum(zeros))/(num_asym);
fprintf('���ټ��� �Ǽ����� ������ ��: %d\n', asym_point)
for k=1:2
    angle = (2*k+1)*pi / num_asym;
    asymptote_angle = rad2deg(atan2(sin(angle), cos(angle)));
    fprintf('���ټ��� ����: %f\n', asymptote_angle)
    % (asym_point, 0) -> (asym_point + 100*cos(angle), 100*sin(angle))
    plot([asym_point, asym_point + 100*cos(angle)], [0, 100*sin(angle)], '--')
end
fprintf('\n')
pause

disp('3. ��� ���� ���ϱ�')
spole = poles(1);
fprintf('��� ��ġ p1 = %f + j%f\n', real(spole), imag(spole))
theta_z1 = atan2(imag(spole - zeros(1)), real(spole - zeros(1)));
theta_p2 = atan2(imag(spole - poles(2)), real(spole - poles(2)));
theta_p3 = atan2(imag(spole - poles(3)), real(spole - poles(3)));
theta_p1 = pi + theta_z1 - theta_p2 - theta_p3;
fprintf('theta_p1 = pi + %f - %f - %f = %f (%f deg)\n\n', ... 
    theta_z1, theta_p2, theta_p3, theta_p1, rad2deg(theta_p1))
plot([real(spole), real(spole) + 2*cos(theta_p1)], ...
    [imag(spole), imag(spole) + 2*sin(theta_p1)], '--')

spole = poles(2);
fprintf('��� ��ġ p1 = %f + j%f\n', real(spole), imag(spole))
theta_z1 = atan2(imag(spole - zeros(1)), real(spole - zeros(1)));
theta_p1 = atan2(imag(spole - poles(1)), real(spole - poles(1)));
theta_p3 = atan2(imag(spole - poles(3)), real(spole - poles(3)));
theta_p2 = -pi + theta_z1 - theta_p1 - theta_p3;
fprintf('theta_p2 = -pi + %f - %f - %f = %f (%f deg)\n\n', ...
    theta_z1, theta_p1, theta_p3, theta_p2, rad2deg(theta_p2))
plot([real(spole), real(spole) + 2*cos(theta_p2)], ...
    [imag(spole), imag(spole) + 2*sin(theta_p2)], '--')

hold off
