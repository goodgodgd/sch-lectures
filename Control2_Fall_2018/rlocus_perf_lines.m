function rlocus_perf_lines(num, den, varargin)
%   num: numerator
%   den: denominator

% �Ķ���� �⺻�� ����
peak_time = 0;
overshoot = 0;
settling_time = 0;
zeta = 0;

% �Է����ڷκ��� �Ķ���� ����
numvarargs = length(varargin)
for i=1:2:numvarargs
    if strcmp(varargin{i}, 'peak_time')
        peak_time = varargin{i+1};
    end
    if strcmp(varargin{i}, 'settling_time')
        settling_time = varargin{i+1};
    end
    if strcmp(varargin{i}, 'overshoot')
        overshoot = varargin{i+1};
    end
    if strcmp(varargin{i}, 'zeta')
        overshoot = varargin{i+1};
    end
end

% �ٱ��� �׸���
Ms = tf(num, den);
figure(1)
subplot(121)
hold off
rlocus(Ms)
hold on

% peak time�� �����ϴ� ������ ǥ��
if peak_time > 0
    wd = pi/peak_time;
    fprintf('peak time %f �� �����ϴ� wd=%f\n', peak_time, wd)
    plot([-100 100], [wd wd], '-.')
end

% settling time�� �����ϴ� ������ ǥ��
if settling_time > 0
    sigma = -4/settling_time;
    fprintf('settling time %f �� �����ϴ� sd=%f\n', settling_time, sigma)
    plot([sigma sigma], [-100 100], '-.')
end

% %OS�� �����ϴ� ������ ǥ��
if overshoot > 0
    zeta = -log(overshoot) / sqrt(pi^2 + log(overshoot));
    theta = pi/2 + asin(zeta);
    fprintf('overshoot %1.1f%% �� �����ϴ� theta=%1.2f deg\n', overshoot*100, rad2deg(theta-pi/2))
    plot([0 100*cos(theta)], [0 100*sin(theta)], '-.')
end

% zeta�� �����ϴ� ������ ǥ��
if zeta > 0
    theta = pi/2 + asin(zeta);
    fprintf('overshoot %1.1f%% �� �����ϴ� theta=%1.2f deg\n', overshoot*100, rad2deg(theta-pi/2))
    plot([0 100*cos(theta)], [0 100*sin(theta)], '-.')
end

Ms = tf(num, den);
[y, t] = step(Ms);
subplot(122)
hold off
plot(t, y)
hold on

end


