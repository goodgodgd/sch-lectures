% 작업공간에 있는 모든 데이터 날리고 새 데이터 준비
clc; clear
x = 0:0.1:10;
y1 = cos(x);
y2 = exp(-x);

disp('cos(x) 는 빨간 점으로 그리고 exp(-x)는 검은 점선으로 그리기')
plot(x, y1, 'r.', x, y2, 'k--')
pause

disp('그래프 속성 표시')
% 그래프 위에 제목 붙이기
title('Control Engineering')

% x, y축 이름 붙이기
xlabel('x축')
ylabel('y축')

% 그래프 영역 지정
axis([0 pi*3 -1.5 1.5])

% 그래프 안에 텍스트 표시
text(2, 1, 'text 함수를 이용한 텍스트 표시')

% 그래프 각 선에 대한 라벨 표시
legend('cos(x)', 'exp(-x)')