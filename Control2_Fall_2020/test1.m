clc
clear

zeta = 0.5
omega = 1
peak_time = pi / (omega * sqrt(1-zeta^2))
os = exp(-pi*zeta / sqrt(1-zeta^5))
