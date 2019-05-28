disp('작업공간에 있는 모든 데이터 날리고 새 데이터 준비')
clc; clear
x = 0:0.1:10;
y1 = cos(x);
y2 = exp(-x);

disp('그래프를 따로 그리면 기존 그래프를 없애고 새로 그리게 됨')
plot(x, y1)
plot(x, y2)
pause

disp('기존 그래프 위에 새 그래프를 그리려면 hold on')
plot(x, y1)
hold on
plot(x, y2)
pause

disp('기존 그래프 유지 해제하려면 hold off')
hold off
plot(x, y1)
pause

disp('새창에 y2 그리려면 figure 함수 이용')
figure
plot(x, y2)

disp('figure 번호를 명시적으로 지정 가능')
figure(2)
plot(x, y2)
