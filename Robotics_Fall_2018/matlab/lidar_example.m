clc; clear

a=-60:5:60;
a=a/180*pi;
y=ones(size(a));
x=y.*tan(a);
plot(x, y, '.')
d=sqrt(x.*x + y.*y);
data=[1:25; a; d; x; y];

hold on
for i=1:25
    plot([0 x(i)], [0 y(i)], 'b-')
end
axis([-2 2 -0.5 1.5])
hold off
