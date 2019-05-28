clc; clear

s = tf('s');
G = (s+6)*(s+8)/((s+1)*(s+4)*(s+10));

% 먼저 근궤적을 그려놓고 근궤적을 검증해보자
figure(1)
rlocus(G)
axis([-12 2 -7 7])
hold on

disp('1. G의 극점 영점 구하기')
poles = pole(G)
zeros = zero(G)
pause

disp('2. 분기점 구하기')
% 전달함수의 분모 분자의 계수 추출
[num, den] = tfdata(G);
num = num{1}
den = den{1}

syms w
K_w = -poly2sym(den, w) / poly2sym(num, w)
disp('심볼릭 함수로 표현한 dK(w)/dw')
dK_w = diff(K_w)
% 근궤적의 교차점 후보 구하기 = dK_w의 분자가 0이 되는 해 구하기
[num, den] = numden(dK_w)  % 분자의 추출
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
