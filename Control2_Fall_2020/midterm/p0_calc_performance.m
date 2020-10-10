den = [1 6 25];
wn = sqrt(den(3))
zeta = den(2)/2/wn
Tp = pi/(wn*sqrt(1-zeta^2))
Ts = 4/(wn*zeta)
OS = exp(-pi*zeta/sqrt(1-zeta^2))
