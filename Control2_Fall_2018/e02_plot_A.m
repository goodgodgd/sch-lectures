% �۾������� �ִ� ��� ������ ������
clc; clear

x = 0:0.1:10;
y1 = cos(x);
y2 = exp(-x);

disp('cos(x) �׸���')
plot(x, y1)
pause

disp('cos(x), exp(-x) ���ÿ� �׸���')
plot(x, y1, x, y2)
pause

disp('cos(x) ���� ������ �׸���')
plot(x, y1, 'r.')
pause

disp('cos(x) �� ���� ������ �׸��� exp(-x)�� ���� �������� �׸���')
plot(x, y1, 'r.', x, y2, 'k--')