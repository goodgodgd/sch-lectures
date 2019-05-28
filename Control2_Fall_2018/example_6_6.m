clc; clear

s = tf('s');
G = 1/(s*(s+1)*(s+4));

% ���� �ٱ����� �׷����� �ٱ����� �����غ���
figure(1)
rlocus(G)
axis([-8 2 -5 5])
hold on

disp('1. G�� ���� ���� ���ϱ�')
poles = pole(G)
zeros = zero(G);
pause

disp('2. �ٱ����� ���ټ� ���ϱ�')
num_asym = size(poles,1) - size(zeros,1);
fprintf('�߻��ϴ� ���ټ��� ����: %d\n', num_asym)
asym_point = (sum(poles) - sum(zeros))/(num_asym);
fprintf('���ټ��� �Ǽ����� ������ ��: %f\n', asym_point)
for k=1:3
    angle = (2*k+1)*pi / num_asym;
    asymptote_angle = rad2deg(atan2(sin(angle), cos(angle)));
    fprintf('���ټ��� ����: %f\n', asymptote_angle)
    % (asym_point, 0) -> (asym_point + 100*cos(angle), 100*sin(angle))
    plot([asym_point, asym_point + 100*cos(angle)], [0, 100*sin(angle)], '--')
end
fprintf('\n')
pause

disp('3. �б��� ���ϱ�')
% �����Լ��� �и� ������ ��� ����
[num, den] = tfdata(G);
num = num{1};
den = den{1};

syms w
K_w = -poly2sym(den, w) / poly2sym(num, w);
disp('�ɺ��� �Լ��� ǥ���� dK(w)/dw')
dK_w = diff(K_w)
% �ٱ����� ������ �ĺ� ���ϱ� = dK_w�� ���ڰ� 0�� �Ǵ� �� ���ϱ�
[num, den] = numden(dK_w);  % ������ ����
num = sym2poly(num);        % ������ ��� ����
breakpts = roots(num)            % ����=0 �� �� ���
for i=1:size(breakpts, 1)
    if ~isreal(breakpts(i))
        continue
    end
    % �б������κ��� �ٽ� K(s_i) ����ϱ�
    K_wi = double(subs(K_w, w, breakpts(i)));
    % �б������� K�� ���� �Ǽ����� �Ѵ�.
    if K_wi > 0
        fprintf('�ٱ����� �������� s = %f �̴�. K = %f\n', breakpts(i), K_wi)
        plot(breakpts(i), 0, 'rd')
    end
end
hold off

