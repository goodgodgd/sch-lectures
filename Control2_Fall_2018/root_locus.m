function root_locus(num, den, varargin)
%   num: numerator
%   den: denominator

% 파라미터 기본값 설정
fig_axis = 'auto';
asymtote = 1;
pz_angle = 1;

% 입력인자로부터 파라미터 설정
numvarargs = length(varargin);
for i=1:2:numvarargs
    if strcmp(varargin{i}, 'fig_axis')
        fig_axis = varargin{i+1};
    end
    if strcmp(varargin{i}, 'aux_lines')
        asymtote = varargin{i+1};
    end
    if strcmp(varargin{i}, 'pz_angle')
        pz_angle = varargin{i+1};
    end
end

% 근궤적 그리기
Ms = tf(num, den);
figure(1)
hold off
rlocus(Ms)
hold on

% pole, zero 계산
poles = pole(Ms);
zeros = zero(Ms);

% 그래프 범위 지정
if strcmp(fig_axis, 'auto')
    pz = [poles; zeros];
    fig_axis = [min(real(pz)), max(real(pz)), min(imag(pz)), max(imag(pz))];
    margin = [min(max(max(real(abs(pz)))*0.2, 2), 10), min(max(max(imag(abs(pz))), 3), 10)];
    fig_axis = [fig_axis(1)-margin(1), fig_axis(2)+margin(1), fig_axis(3)-margin(2), fig_axis(4)+margin(2)];
end
axis(fig_axis)

% 점근선 그리기
if asymtote == 1
    % 점근선 그리기
    num_asym = size(poles,1) - size(zeros,1);
    if num_asym > 2
        fprintf('발산하는 점근선의 개수: %d\n', num_asym)
        asym_point = (sum(poles) - sum(zeros))/(num_asym);
        fprintf('점근선과 실수축이 만나는 점: %f\n', asym_point)
        for k=1:num_asym
            angle = (2*k+1)*pi / num_asym;
            asymptote_angle = rad2deg(atan2(sin(angle), cos(angle)));
            fprintf('점근선의 각도 %d: %f\n', k, asymptote_angle)
            plot([asym_point, asym_point + 100*cos(angle)], [0, 100*sin(angle)], '--')
        end
    end
end

% 분기점 계산

% 출발각, 도착각 그리기
if pz_angle == 1
    % 출발각
    not_on_real_axis = abs(imag(poles)) > 0;
    for i=1:length(poles)
        % 실수가 아닌 복소수일 때만 출발각 계산
        if not_on_real_axis(i) == 0
            continue            
        end
        angle_sum = 0;
        curpole = poles(i);
        % 다른 극점과의 각도 합산 빼기
        for k=1:length(poles)
            if i ~= k
                pole_ang = atan2(imag(curpole - poles(k)), real(curpole - poles(k)));
                angle_sum = angle_sum - pole_ang;
            end
        end
        % 다른 영점과의 각도 합산 더하기
        for k=1:length(zeros)
            zero_ang = atan2(imag(curpole - zeros(k)), real(curpole - zeros(k)));
            angle_sum = angle_sum + zero_ang;
        end
        % angle_sum - depart_ang = pi
        depart_ang = angle_sum - pi;
        depart_ang = atan2(sin(depart_ang), cos(depart_ang));
        fprintf('극점: %f+j%f, 출발각: %f, 나머지각 합산: %f\n', real(curpole), imag(curpole), depart_ang, angle_sum)
        
        cur_x = real(curpole);
        cur_y = imag(curpole);
        plot([cur_x, cur_x+cos(depart_ang)], [cur_y, cur_y+sin(depart_ang)], '--')
    end
    
    % 도착각
    not_on_real_axis = abs(imag(zeros)) > 0;
    for i=1:length(zeros)
        % 실수가 아닌 복소수일 때만 출발각 계산
        if not_on_real_axis(i) == 0
            continue            
        end
        angle_sum = 0;
        curzero = zeros(i);
        % 다른 극점과의 각도 합산 빼기
        for k=1:length(poles)
                pole_ang = atan2(imag(curzero - poles(k)), real(curzero - poles(k)));
                angle_sum = angle_sum - pole_ang;
        end
        % 다른 영점과의 각도 합산 더하기
        for k=1:length(zeros)
            if i ~= k
                zero_ang = atan2(imag(curzero - zeros(k)), real(curzero - zeros(k)));
                angle_sum = angle_sum + zero_ang;
            end
        end
        % angle_sum + arrival_ang = pi
        arrival_ang = pi - angle_sum;
        arrival_ang = atan2(sin(arrival_ang), cos(arrival_ang));
        fprintf('영점: %f+j%f, 도착각: %f, 나머지각 합산: %f\n', real(curzero), imag(curzero), arrival_ang, angle_sum)
        
        cur_x = real(curzero);
        cur_y = imag(curzero);
        plot([cur_x, cur_x+cos(arrival_ang)], [cur_y, cur_y+sin(arrival_ang)], '--')
    end    
end

end % function

