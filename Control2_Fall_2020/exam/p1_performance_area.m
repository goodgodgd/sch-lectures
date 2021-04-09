clc; clear
s= tf('s');
GH = (s^+ 2*s + 50) / ((s+1) * ( s^2 + 4*s + 11))
pause

clc; clear

% 좌표 축만 그리기
range = [-6 2 -4 4];
draw_axis(range)
pause

% 기준선 예시 그림
draw_axis(range)
draw_settle_time_line(3, 'r--')
draw_overshoot_line(17, 'g--')
draw_peak_time_line(2, 'b--')
pause

% 1-1 성능 기준선 그리기
fprintf('>>>>> 1-1 \n')
draw_axis(range)
draw_settle_time_line(4, 'r--')
draw_overshoot_line(10, 'g--')
pause

% 1-2 성능 기준선 그리기
fprintf('>>>>> 1-2 \n')
draw_axis(range)
draw_peak_time_line(2, 'b--')
draw_overshoot_line(15, 'g--')

 
function draw_axis(range)
    % 축 그리기
    plot([0 0], [-100 100], '-k')
    hold on
    plot([-100 100], [0 0], '-k')
    % 위치 고정
    hold off
    axis(range)
    set(gcf,'Position',[200 200 400 400])
end

function draw_peak_time_line(tp, style)
    wd = pi/tp;
    fprintf('Tp<%.4f, wd>%.4f\n', tp, wd)
    hold on
    plot([-100, 100], [wd, wd], style)
    plot([-100, 100], [-wd, -wd], style)
    hold off
end

function draw_settle_time_line(ts, style)
    sigmad = 4/ts;
    fprintf('Ts<%.4f, sigmad>%.4f\n', ts, sigmad)
    hold on
    plot([-sigmad, -sigmad], [-100, 100], style)
    hold off
end

function draw_overshoot_line(os, style)
    zeta = sqrt(log(os/100)^2 / (log(os/100)^2 + pi^2));
    theta = acos(zeta);
    fprintf('%%OS<%.1f, zeta>%.4f, theta<%.4f(deg)\n', os, zeta, rad2deg(theta))
    hold on
    plot([0 -100*cos(theta)], [0  100*sin(theta)], style)
    plot([0 -100*cos(theta)], [0 -100*sin(theta)], style)
    hold off
end
