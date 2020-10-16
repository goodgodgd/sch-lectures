clc; clear
% ���� ����
s = tf('s');
otf = 1/((s+1)*(s+4)*(s+6))
% �ִ��ʰ� ����
os = 0.16;
% �����ð�
ts = 2;

% �ٱ��� �׸���
figure(1)
subplot(1,3,1)
rlocus(otf)
hold on

fprintf('>>>>> ��ǥ ���� ���� \n')
[zeta, theta] = draw_overshoot_line(os, 'b--');
sigma_d = draw_settle_time_line(ts, 'r--');

wn = sigma_d/zeta;
pole_real = -sigma_d;
pole_imag = wn*sqrt(1-zeta^2);
target_pole = pole_real + 1i*pole_imag;
fprintf('�ִ��ʰ��� �����ð��� �����ϴ� ������ ��ġ s = %.4f + j%.4f\n', ...
        pole_real, pole_imag)
plot(pole_real, pole_imag, 'rd')
hold off
axis([-12 2 -7 7])
title('�⺻ �ٱ����� ���� ����')

% PD ������� ���� ����
zero_pd = design_pd_controller(otf, target_pole);

% PD ����⸦ �ݿ��� �ٱ���
subplot(1,3,2)
otf_pd = otf * (s - zero_pd)
rlocus(otf_pd)
hold on
plot(real(target_pole), imag(target_pole), 'rd')
hold off
title('PD ���� �� �ٱ���')
axis([-12 2 -7 7])
K = -1/evalfr(otf_pd, target_pole);
fprintf("PD ����� ���� �� target pole������ ��� �̵� K=%1.4f\n", K)

fprintf('\n>>>>> ������� ������ 0���� ����� PI ����� ���� \n')
zero_pi = 0.1;
fprintf('PI ������� ���� ��ġ ����: %.1f\n', zero_pi)

% PID ����⸦ �ݿ��� �ٱ���
subplot(1,3,3)
otf_pid = otf_pd * (s + zero_pi) / s;
rlocus(otf_pid)
hold on
plot(real(target_pole), imag(target_pole), 'rd')

K = find_K(otf_pid, target_pole);
fprintf('���� PID �����: K=%.4f\n', K)
otf_final = otf_pid * K
find_closed_pole(otf_final)

hold off
axis([-12 2 -7 7])
title('PID ���� �� �ٱ���')
set(gcf,'Position',[200 200 1600 400])


function [zeta, theta] = draw_overshoot_line(os, style)
    zeta = sqrt(log(os)^2 / (log(os)^2 + pi^2));
    theta = acos(zeta);
    fprintf('%%OS=%.1f, zeta=%.4f, theta=%.3f(deg)\n', os, zeta, rad2deg(theta))
    plot([0 -100*cos(theta)], [0  100*sin(theta)], style)
    plot([0 -100*cos(theta)], [0 -100*sin(theta)], style)
end

function sigma_d = draw_settle_time_line(ts, style)
    sigma_d = 4/ts;
    fprintf('Ts=%.4f, |real(pole)|=%.4f\n', ts, sigma_d)
    plot([-sigma_d, -sigma_d], [-100, 100], style)
end

function K = find_K(otf, pole_pos)
    [num, den] = tfdata(otf);
    num = num{1};
    den = den{1};
    syms w
    K_w = -poly2sym(den, w) / poly2sym(num, w);
    K = real(double(subs(K_w, w, pole_pos)));
end

function find_closed_pole(otf)
    % ����� ���Խ� target_pole�� �������� �������� ����
    [num, den] = tfdata(otf);
    chareq = den{1} + num{1};
    disp('PID ����� �ݿ��Ͽ� ��ü �ý��� T(s)�� ���� ���')
    verify_poles = roots(chareq)
    for pole=verify_poles
        plot(real(pole), imag(pole), 'b>')
    end
end

function zero_pd = design_pd_controller(otf, target_pole)
    fprintf('\n>>>>> �ٱ����� ��ǥ ������ ������ �ϴ� PD ����� ���� \n')
    disp('��ǥ ���������� ������ �����Լ� ���� ���')
    phase_G = 0;
    zero_otf = zero(otf);
    pole_otf = pole(otf);
    if ~isempty(zero_otf)
        for i=1:size(zeros_otf,1)
            vector = target_pole - zero_otf(i);
            zero_phase = atan2(imag(vector), real(vector));
            phase_G = phase_G + zero_phase;
            fprintf('������ ���� angle(s - (%.3f + j%.3f)) = %.3f rad\n', ...
                    real(zero_otf(i)), imag(zero_otf(i)), zero_phase)
        end
    end
    for i=1:size(pole_otf,1)
        vector = target_pole - pole_otf(i);
        pole_phase = atan2(imag(vector), real(vector));
        phase_G = phase_G - pole_phase;
        fprintf('������ ���� angle(s - (%.3f + j%.3f)) = %.3f(deg)\n', ...
                real(pole_otf(i)), imag(pole_otf(i)), rad2deg(pole_phase))
    end
    fprintf('���� s = %.3f + j%.3f ���� G(s)�� ���� = %.1f(deg) = %.3f(rad)\n', ...
            real(target_pole), imag(target_pole), rad2deg(phase_G), phase_G)
    phase_PD = -pi - phase_G;
    fprintf('PD ����Ⱑ �������� ���� = %.3f - (%.3f) = %.4f(rad) = %.3f(deg)\n', ...
            pi, phase_G, phase_PD, rad2deg(phase_PD))
    zero_pd = real(target_pole) - imag(target_pole)/tan(phase_PD);
    fprintf('PD ������� ���� ��ġ = %.4f\n', zero_pd)
end
