clc; clear;
% 모든 figure 창 닫기
close all
% 데이터 준비
x = 0:0.1:10;
y1 = cos(x);
y2 = sin(x);
y3 = exp(-x);
y4 = log(x);

% figure(1)
subplot(2,2,1)
plot(x, y1)
title('cosine')

subplot(2,2,2)
plot(x, y2)
title('sine')

subplot(2,2,3)
plot(x, y3)
title('exponential')

subplot(2,2,4)
plot(x, y4, 'r.')
title('log')
