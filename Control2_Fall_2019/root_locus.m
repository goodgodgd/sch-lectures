function root_locus(num, den, varargin)
%   num: numerator
%   den: denominator

% �Ķ���� �⺻�� ����
fig_axis = 'auto';
asymtote = 1;
pz_angle = 1;

% �Է����ڷκ��� �Ķ���� ����
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

% �ٱ��� �׸���
Ms = tf(num, den);
figure(1)
hold off
rlocus(Ms)
hold on

% pole, zero ���
poles = pole(Ms);
zeros = zero(Ms);

% �׷��� ���� ����
if strcmp(fig_axis, 'auto')
    pz = [poles; zeros];
    fig_axis = [min(real(pz)), max(real(pz)), min(imag(pz)), max(imag(pz))];
    margin = [min(max(max(real(abs(pz)))*0.2, 2), 10), min(max(max(imag(abs(pz))), 3), 10)];
    fig_axis = [fig_axis(1)-margin(1), fig_axis(2)+margin(1), fig_axis(3)-margin(2), fig_axis(4)+margin(2)];
end
axis(fig_axis)

% ���ټ� �׸���
if asymtote == 1
    % ���ټ� �׸���
    num_asym = size(poles,1) - size(zeros,1);
    if num_asym > 2
        fprintf('�߻��ϴ� ���ټ��� ����: %d\n', num_asym)
        asym_point = (sum(poles) - sum(zeros))/(num_asym);
        fprintf('���ټ��� �Ǽ����� ������ ��: %f\n', asym_point)
        for k=1:num_asym
            angle = (2*k+1)*pi / num_asym;
            asymptote_angle = rad2deg(atan2(sin(angle), cos(angle)));
            fprintf('���ټ��� ���� %d: %f\n', k, asymptote_angle)
            plot([asym_point, asym_point + 100*cos(angle)], [0, 100*sin(angle)], '--')
        end
    end
end

% �б��� ���

% ��߰�, ������ �׸���
if pz_angle == 1
    % ��߰�
    not_on_real_axis = abs(imag(poles)) > 0;
    for i=1:length(poles)
        % �Ǽ��� �ƴ� ���Ҽ��� ���� ��߰� ���
        if not_on_real_axis(i) == 0
            continue            
        end
        angle_sum = 0;
        curpole = poles(i);
        % �ٸ� �������� ���� �ջ� ����
        for k=1:length(poles)
            if i ~= k
                pole_ang = atan2(imag(curpole - poles(k)), real(curpole - poles(k)));
                angle_sum = angle_sum - pole_ang;
            end
        end
        % �ٸ� �������� ���� �ջ� ���ϱ�
        for k=1:length(zeros)
            zero_ang = atan2(imag(curpole - zeros(k)), real(curpole - zeros(k)));
            angle_sum = angle_sum + zero_ang;
        end
        % angle_sum - depart_ang = pi
        depart_ang = angle_sum - pi;
        depart_ang = atan2(sin(depart_ang), cos(depart_ang));
        fprintf('����: %f+j%f, ��߰�: %f, �������� �ջ�: %f\n', real(curpole), imag(curpole), depart_ang, angle_sum)
        
        cur_x = real(curpole);
        cur_y = imag(curpole);
        plot([cur_x, cur_x+cos(depart_ang)], [cur_y, cur_y+sin(depart_ang)], '--')
    end
    
    % ������
    not_on_real_axis = abs(imag(zeros)) > 0;
    for i=1:length(zeros)
        % �Ǽ��� �ƴ� ���Ҽ��� ���� ��߰� ���
        if not_on_real_axis(i) == 0
            continue            
        end
        angle_sum = 0;
        curzero = zeros(i);
        % �ٸ� �������� ���� �ջ� ����
        for k=1:length(poles)
                pole_ang = atan2(imag(curzero - poles(k)), real(curzero - poles(k)));
                angle_sum = angle_sum - pole_ang;
        end
        % �ٸ� �������� ���� �ջ� ���ϱ�
        for k=1:length(zeros)
            if i ~= k
                zero_ang = atan2(imag(curzero - zeros(k)), real(curzero - zeros(k)));
                angle_sum = angle_sum + zero_ang;
            end
        end
        % angle_sum + arrival_ang = pi
        arrival_ang = pi - angle_sum;
        arrival_ang = atan2(sin(arrival_ang), cos(arrival_ang));
        fprintf('����: %f+j%f, ������: %f, �������� �ջ�: %f\n', real(curzero), imag(curzero), arrival_ang, angle_sum)
        
        cur_x = real(curzero);
        cur_y = imag(curzero);
        plot([cur_x, cur_x+cos(arrival_ang)], [cur_y, cur_y+sin(arrival_ang)], '--')
    end    
end

end % function

