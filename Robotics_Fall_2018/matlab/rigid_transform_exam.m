clc; clear
% pose2 in frame 1
pose1_2 = [5, -1, -pi/3];
theta = pose1_2(3);
R1 = [cos(theta), -sin(theta); sin(theta), cos(theta)];
t1_2 = [pose1_2(1); pose1_2(2)];
% transformation matrix of pose2 in frame 1
T1_2 = [R1 t1_2; 0 0 1]

% pose3 in frame 2
pose2_3 = [1, -4, -pi/6];
theta = pose2_3(3);
R2_3 = [cos(theta), -sin(theta); sin(theta), cos(theta)];
t2_3 = [pose2_3(1); pose2_3(2)];
% transformation matrix of pose3 in frame 2
T2_3 = [R2_3 t2_3; 0 0 1]

% pose2 in global frame
T1_3 = T1_2 * T2_3

disp('transform point a in frame 2 to frame 1')
pa_2 = [-2,2,1]';
pa_1 = T1_2 * pa_2
disp('transform point a in frame 2 to frame 3')
T3_2 = inv(T2_3)
pa_3 = T2_3 \ pa_2

disp('transform point b in frame 3 to frame 2')
pb_3 = [2,3,1]';
pb_2 = T2_3 * pb_3
disp('transform point b in frame 3 to frame 1')
pb_1 = T1_3 * pb_3

% draw frames and points
% x, y axes in homogeneous coordinates
baisic_axes = [0 0 1; 1 0 1; 0 1 1]';
frameg = baisic_axes;   % in global frame
frame1 = T1_2 * baisic_axes; % transform to frame1
frame2 = T1_3 * baisic_axes; % transform to frame2

% plot global frame with blue line
hold off
plot(frameg(1, [1 2]), frameg(2, [1 2]), 'b-', frameg(1, [1 3]), frameg(2, [1 3]), 'b-')
text(frameg(1, 1), frameg(2, 1)-0.1, 'global frame')
hold on
% plot frame1 with red line
plot(frame1(1, [1 2]), frame1(2, [1 2]), 'r-', frame1(1, [1 3]), frame1(2, [1 3]), 'r-')
text(frame1(1, 1), frame1(2, 1)-0.1, 'frame1')
% plot frame2 with black line
plot(frame2(1, [1 2]), frame2(2, [1 2]), 'k-', frame2(1, [1 3]), frame2(2, [1 3]), 'k-')
text(frame2(1, 1), frame2(2, 1)-0.1, 'frame2')

% mark points
plot(pa_1(1), pa_1(2), '*')
plot(pb_1(1), pb_1(2), '*')
