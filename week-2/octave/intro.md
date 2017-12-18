## Basics
v = 1:6 % [1 2 3 4 5 6]
v = 1:0.1:2 =
 Columns 1 through 8:
    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000    1.6000    1.7000
 Columns 9 through 11:
    1.8000    1.9000    2.0000

ones(2,3)
1 1 1
1 1 1 

ones(1,3)
1 1 1

zeros(1,3)
0 0 0

rand(3,3) % random 3x3

w = randn(1, 2) % gaussian distribution

w = -6 + (sqrt(10) * (randn(1, 10000))
hist(w) % draw graph, very useful

eye(3) % identity mat

1 0 0
0 1 0
0 0 1

help eye % get help

size((eye(3)) % [3, 3]
size([9, 9]) % [1, 2]

## Reading and writing files
`load featuresX.dat` % load some data
`load ('featuresX.dat')` % load some data

who % current variables
whos % variables with more info
clear x % delete variable `x`
clear % clear all

`save hello.mat x` % save variable x to hello.mat
`save hello.mat x v` % save variable x to hello.mat compressed
`save hello.txt x v -ascii` % save human readable

A =
1 2
3 4
5 6 

A(3,2) % 6
A(:,2) [2 4 6] 
A([1, 3], :) % [1 2; 5 6]
A = [A, [100; 200; 300]] % append

A =
1 2 100
3 4 200
5 6 300

## Plotting

t = [0 : 0.01 : -.98]
y1 = sin(2 * pi * 4 * t)
plot(t, y1)
y2 = cos(2 * pi * 4 * t)
hold on;
plot(t, y2)
xlabel('time')
ylabel('value')
legend('sin', 'cos')
title('my plot') 
print -dpng 'myPlot.png' % Save file

subplot(1, 2, 1) % divide plot into 1x2 grid, access first element
axis([0.5, 1 -1 1])  % set range of axis

clf % clear figure
A = magic(5)
imagesc(A)
imagesc(A), colorbar, colormap gray
