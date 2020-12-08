clc; clear

% ���� ����
s = tf('s');
otf = 1/((s+1)*(s+5))
% �ִ��ʰ� ����
os = 0.15;

% �ٱ��� �׸���
figure(1)
rlocus(otf)
hold on

% ���ټ��� �Ǽ����� ������ ���
poles = pole(otf);
zeros = zero(otf);
disp(poles')
num_asym = size(poles,1) - size(zeros,1);
fprintf('�߻��ϴ� ���ټ��� ����: %d\n', num_asym)
asym_point = (sum(poles) - sum(zeros))/(num_asym);
fprintf('���ټ��� �Ǽ����� ������ ��: %.1f\n', asym_point)

% ��ǥ ������ �Ǽ���
pole_real = asym_point;
fprintf('�б���=���ټ� ������ �϶�, ������ �Ǽ��� real(p) = %.1f\n', pole_real)
% ��ǥ ������ ��� ���� ���ϱ�
[zeta, theta] = draw_overshoot_line(os, 'r--');
pole_imag = abs(pole_real * tan(theta));
fprintf('������ �����ϴ� ������ ��ġ = %.4f + j%.4f\n', pole_real, pole_imag)
% ��ǥ ���� �׸���
plot(pole_real, pole_imag, 'rd')
target_pole = pole_real + 1i*pole_imag;

% target pole�� ������ K�� ���ϱ�
K = find_K(otf, target_pole);
fprintf('��ǥ ���������� K ��: %.4f\n', K)

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