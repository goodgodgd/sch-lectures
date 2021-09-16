clc
time = out.pid_result1.time;
p_cont = out.pid_result1.signals(1).values;
pd_cont = out.pid_result1.signals(2).values;
pid_cont = out.pid_result1.signals(3).values;

plot(time, p_cont, time, pd_cont, time, pid_cont)

tp = 0.3;
os = 0.2;
steady = 856.5 / 1007;
peak = steady * 1.2;

hold on
plot([tp, tp], [0, 1.2], 'g--')
plot([0, 10], [steady, steady], 'm--')
plot([0, 10], [peak, peak], 'm--')
hold off
