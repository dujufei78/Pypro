# -*- coding: utf-8 -*-
----------------- lua基础   -----------------------------

-- 变量
a = 3
local b=4

function joke()
    c = 9
    local d = 7
end

joke()
print(c, d)

do
    local a = 6
    b = 9
    print(a, b)

end

print(a, b)

-- while 循环

a = 10
while(a<20)
do
    print('a的值为：', a)
    a = a + 1
end

-- for循环


for i =10, 2, -1 do
    print(i)
end


b = {a=1, c=2}
for k, v in pairs(b) do
    print('--d---')

    print(k, v)
end


-- repeat unti=l

a = 10
repeat
    print('a的值为：', a)
    a = a + 1
until(a > 15)

-- 函数

myprint = function(param)
    print('这是打印函数--', param, '##')
end

function add(num1, num2, functionPrint)
    result = num1 + num2
    functionPrint(result)
end

add(3, 6, myprint)

-- 函数多返回值
--function maximum (a)
--    local mi = 1



-- 标准库
local a = {'a', 'b', 'c'}
print(table.concat(a))

-- math模块
math.randomseed(os.time())
print(math.random())
print(math.random(100))

-- 虚变量
local start = string.find('hello', 'he')
print(start)

local _, end_pos = string.find('hello', 'hel')
print(end_pos)

print('----')
for _, v in ipairs({3,4,6}) do
    print(v)
end

-- 下标
t = {1440}
print(type(t[0]))
print(type(t[2]))

-- 拼接
print('hello' .. ',world')

-- lua中只有一种数据结构，就是table,可以包含数组和哈希表
local color = {first = 'red', 'blue', third = 'green', 'yellow'}
print(color['first'])
print(color[1])
print(color['third'])
print(color[2])
print(color[3])

-- local t1 = {1, a = 2, 3}
-- print('test1' .. table.getn(t1))

local s = 'hi'
--local xxx = require('xxx')
--require('xxx')