clc; clear; close all
% 전달함수 만들기
s = tf('s');
G1 = tf(10);
G2 = s+6;
G3 = 1/s;
G4 = 1/(s+3);
G = G1*G2*G3*G4

bode(G1, G2, G3, G4)
legend('G1', 'G2', 'G3', 'G4')
grid on
set(gcf,'Position',[200 100 500 400])

pause

bode(G)
grid on
set(gcf,'Position',[200 100 500 400])

pause

subplot(211)
semilogx(-100, 0)
grid on
axis([0.1 100, -40 60])
ylabel('크기(dB)')

subplot(212)
semilogx(-100, 0)
grid on
axis([0.1 100, -40 60])
ylabel('위상(deg)')
xlabel('주파수 (rad/s)')

pause

subplot(211)
semilogx(-100, 0)
grid on
axis([0.1 100, -40 60])
ylabel('크기(dB)')

subplot(212)
semilogx(-100, 0)
grid on
axis([0.1 100, -120 -60])
ylabel('위상(deg)')
xlabel('주파수 (rad/s)')
