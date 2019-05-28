clc; clear

s = tf('s');
G = (s+6)*(s+8)/((s+1)*(s+4)*(s+10));

% ���� �ٱ����� �׷����� �ٱ����� �����غ���
figure(1)
rlocus(G)
axis([-12 2 -7 7])
hold on

disp('1. G�� ���� ���� ���ϱ�')
poles = pole(G)
zeros = zero(G)
pause

disp('2. �б��� ���ϱ�')
% �����Լ��� �и� ������ ��� ����
[num, den] = tfdata(G);
num = num{1}
den = den{1}

syms w
K_w = -poly2sym(den, w) / poly2sym(num, w)
disp('�ɺ��� �Լ��� ǥ���� dK(w)/dw')
dK_w = diff(K_w)
% �ٱ����� ������ �ĺ� ���ϱ� = dK_w�� ���ڰ� 0�� �Ǵ� �� ���ϱ�
[num, den] = numden(dK_w)  % ������ ����
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
