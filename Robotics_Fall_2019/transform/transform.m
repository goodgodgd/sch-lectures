clc; clear

Tg_a = transform_mat(2,3,pi/3)
Ta_b = transform_mat(4,-1,-pi/6)
Tb_c = transform_mat(3,-3,-pi/3)

Tg_b = Tg_a * Ta_b
Tg_c = Tg_b * Tb_c

p_b = [5 1 1]';
p_a = Ta_b * p_b
p_c = Tb_c \ p_b

function mat = transform_mat(x, y, theta)
    mat = [cos(theta) -sin(theta) x;
           sin(theta) cos(theta)  y;
           0 0 1];
end
