clc; clear

s = tf('s');
G = 1/(s*(s+1)*(s+4));

% 먼저 근궤적을 그려놓고 근궤적을 검증해보자
figure(1)
rlocus(G)
axis([-8 2 -5 5])
hold on

disp('1. G의 극점 영점 구하기')
poles = pole(G)
zeros = zero(G);
pause

disp('2. 근궤적의 점근선 구하기')
num_asym = size(poles,1) - size(zeros,1);
fprintf('발산하는 점근선의 개수: %d\n', num_asym)
asym_point = (sum(poles) - sum(zeros))/(num_asym);
fprintf('점근선과 실수축이 만나는 점: %f\n', asym_point)
for k=1:3
    angle = (2*k+1)*pi / num_asym;
    asymptote_angle = rad2deg(atan2(sin(angle), cos(angle)));
    fprintf('점근선의 각도: %f\n', asymptote_angle)
    % (asym_point, 0) -> (asym_point + 100*cos(angle), 100*sin(angle))
    plot([asym_point, asym_point + 100*cos(angle)], [0, 100*sin(angle)], '--')
end
fprintf('\n')
pause

disp('3. 분기점 구하기')
% 전달함수의 분모 분자의 계수 추출
[num, den] = tfdata(G);
num = num{1};
den = den{1};

syms w
K_w = -poly2sym(den, w) / poly2sym(num, w);
disp('심볼릭 함수로 표현한 dK(w)/dw')
dK_w = diff(K_w)
% 근궤적의 교차점 후보 구하기 = dK_w의 분자가 0이 되는 해 구하기
[num, den] = numden(dK_w);  % 분자의 추출
num = sym2poly(num);        % 분자의 계수 추출
breakpts = roots(num)            % 분자=0 의 해 계산
for i=1:size(breakpts, 1)
    if ~isreal(breakpts(i))
        continue
    end
    % 분기점으로부터 다시 K(s_i) 계산하기
    K_wi = double(subs(K_w, w, breakpts(i)));
    % 분기점에서 K는 양의 실수여야 한다.
    if K_wi > 0
        fprintf('근궤적의 교차점은 s = %f 이다. K = %f\n', breakpts(i), K_wi)
        plot(breakpts(i), 0, 'rd')
    end
end
hold off

