clc; clear

t=0:0.01:pi*8;

x1 = cos(pi*t);
x2 = 2*cos(2*pi*t+pi/3);
x3 = 0.5*cos(3*pi*t+pi/4);
x4 = x1+x2+x3;

figure(1)
subplot(5, 1, [1 2])
plot(t, x4)
title('x=x1+x2+x3')
axis([0, pi*6, -4, 4])
subplot(5, 1, 3)
plot(t, x1)
title('x1=cos(pi*t)')
axis([0, pi*6, -2, 2])
subplot(5, 1, 4)
plot(t, x2)
title('x2=2*cos(2pi*t+pi/3)')
axis([0, pi*6, -2, 2])
subplot(5, 1, 5)
plot(t, x3)
title('x3=0.5*cos(3pi*t+pi/4)')
axis([0, pi*6, -2, 2])
