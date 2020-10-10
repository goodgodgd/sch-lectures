clc; clear

range = [-12 2 -7 7];

% 축 그리기
plot([0 0], [-100 100], '-k')
hold on
plot([-100 100], [0 0], '-k')
axis(range)
set(gcf,'Position',[200 200 400 400])
hold off
