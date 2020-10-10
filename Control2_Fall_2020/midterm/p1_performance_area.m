clc; clear

% 축 그리기
plot([0 0], [-100 100], '-k')
hold on
plot([-100 100], [0 0], '-k')

% 성능 기준선 그리기
draw_settle_time_line(2, 'r--')
draw_overshoot_line(15, 'g--')

% 위치 고정
hold off
axis([-8 2 -5 5])
set(gcf,'Position',[200 200 400 400])

pause

% 축 그리기
plot([0 0], [-100 100], '-k')
hold on
plot([-100 100], [0 0], '-k')

% 성능 기준선 그리기
draw_peak_time_line(1, 'b--')
draw_overshoot_line(20, 'g--')

% 위치 고정
hold off
axis([-8 2 -5 5])
set(gcf,'Position',[200 200 400 400])


function draw_peak_time_line(tp, style)
    wd = pi/tp;
    fprintf('Tp<%.4f, wd>%.4f\n', tp, wd)
    plot([-100, 100], [wd, wd], style)
    plot([-100, 100], [-wd, -wd], style)
end

function draw_settle_time_line(ts, style)
    sigmad = 4/ts;
    fprintf('Ts<%.4f, sigmad>%.4f\n', ts, sigmad)
    plot([-sigmad, -sigmad], [-100, 100], style)
end

function draw_overshoot_line(os, style)
    zeta = sqrt(log(os/100)^2 / (log(os/100)^2 + pi^2));
    theta = acos(zeta);
    fprintf('%%OS<%.1f, zeta>%.4f, theta<%.4f(deg)\n', os, zeta, rad2deg(theta))
    plot([0 -100*cos(theta)], [0  100*sin(theta)], style)
    plot([0 -100*cos(theta)], [0 -100*sin(theta)], style)
end
