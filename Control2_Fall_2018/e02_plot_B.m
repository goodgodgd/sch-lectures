disp('�۾������� �ִ� ��� ������ ������ �� ������ �غ�')
clc; clear
x = 0:0.1:10;
y1 = cos(x);
y2 = exp(-x);

disp('�׷����� ���� �׸��� ���� �׷����� ���ְ� ���� �׸��� ��')
plot(x, y1)
plot(x, y2)
pause

disp('���� �׷��� ���� �� �׷����� �׸����� hold on')
plot(x, y1)
hold on
plot(x, y2)
pause

disp('���� �׷��� ���� �����Ϸ��� hold off')
hold off
plot(x, y1)
pause

disp('��â�� y2 �׸����� figure �Լ� �̿�')
figure
plot(x, y2)

disp('figure ��ȣ�� ��������� ���� ����')
figure(2)
plot(x, y2)
