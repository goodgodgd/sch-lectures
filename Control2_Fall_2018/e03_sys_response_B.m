clc; clear
% �ý��� �����Լ� ����
s=tf('s');
G_s=4*(s+2)/(s*(s+3)*(s+7))

% ���� ��ȯ �ý����� �����Լ�
sys=feedback(G_s,1)

% ���� ��� ���� ��� y=���, t=�ð�
[y,t]=step(sys);

% �Էµ����� �����: ��½ð��� ���̸�ŭ 1�� �迭 ����
u=ones(size(t));

% �Է�(u)�� ���(y) �׸���
plot(t,u,'r-', t,y,'b-')
axis([0 15 0 1.1])
xlabel('Time(sec)')
ylabel('Amplitude')
title('Unity Feedback System: Step function')
grid
