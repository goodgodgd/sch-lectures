clc; clear; close all

t=0:0.01:5;
y= 2*cos(pi*t+pi/2);
plot(t, y, 'b-')
hold on
plot([-100, 100], [0, 0], 'k-', [0, 0], [-100, 100], 'k-')
plot([0, 1.5], [2, 2], 'g--', [1.5, 1.5], [0, 2], 'g--')
hold off
axis([0, 5, -2.5, 2.5])
xlabel('t')
ylabel('x(t)')

pause

pt = [-2, 0; 0, 2; 0, 1; 1, 1; 1, 2; 3, 2; 3, -2; 5, 0];
plot([-100, 100], [0, 0], 'k-', [0, 0], [-100, 100], 'k-')
hold on
plot(pt(:,1), pt(:,2), 'b-')
hold off
axis([-3, 6, -2.5, 2.5])
xlabel('t')
ylabel('x(t)')

pause

hpt = [-2, 0; -2, -2; 0, -2; 0, 2; 2, 2; 2, 0];
t = 0:0.01:2;
x = exp(-2*t);

subplot(1,2,1)
plot([-100, 100], [0, 0], 'k-', [0, 0], [-100, 100], 'k-')
hold on
plot(hpt(:,1), hpt(:,2), 'b-')
hold off
axis([-3, 3, -3, 3])
xlabel('t')
ylabel('h(t)')

subplot(1,2,2)
plot([-100, 100], [0, 0], 'k-', [0, 0], [-100, 100], 'k-')
hold on
plot(t, x, 'b-')
hold off
axis([-3, 3, -3, 3])
xlabel('t')
ylabel('x(t)')
