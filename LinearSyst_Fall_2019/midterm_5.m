clc; clear

ht = [-2, 0; -2, 2; 0, 2; 0, -2; 2, -2; 2, 0];
figure(1)
subplot(1,2,1)
plot(ht(:,1), ht(:,2), 'b')
hold on
plot([-100, 100], [0, 0], 'k', [0, 0], [-100, 100], 'k')
hold off
axis([-3, 3, -3, 3])
ylabel('h(t)')
xlabel('t')

t = 0:0.01:5;
xt = 2*exp(-t);
subplot(1,2,2)
plot(t, xt, 'b')
hold on
plot([-100, 100], [0, 0], 'k', [0, 0], [-100, 100], 'k')
hold off
axis([-3, 3, -3, 3])
ylabel('x(t)')
xlabel('t')

htau = ht;
htau(:,2) = -ht(:,2);
figure(2)
subplot(2,2,1)
plot(t, xt, 'b')
hold on
plot(htau(:,1)-3, htau(:,2), 'r')
plot([-100, 100], [0, 0], 'k', [0, 0], [-100, 100], 'k')
hold off
axis([-6, 6, -3, 3])
xlabel('t<-2')
grid on

subplot(2,2,2)
plot(t, xt, 'b')
hold on
plot(htau(:,1)-1, htau(:,2), 'r')
plot([-100, 100], [0, 0], 'k', [0, 0], [-100, 100], 'k')
hold off
axis([-6, 6, -3, 3])
xlabel('-2<t<0')
grid on

subplot(2,2,3)
plot(t, xt, 'b')
hold on
plot(htau(:,1)+1, htau(:,2), 'r')
plot([-100, 100], [0, 0], 'k', [0, 0], [-100, 100], 'k')
hold off
axis([-6, 6, -3, 3])
xlabel('0<t<2')
grid on

subplot(2,2,4)
plot(t, xt, 'b')
hold on
plot(htau(:,1)+3, htau(:,2), 'r')
plot([-100, 100], [0, 0], 'k', [0, 0], [-100, 100], 'k')
hold off
axis([-6, 6, -3, 3])
xlabel('t>2')
grid on
