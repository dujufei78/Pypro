--------------------    菜鸟教程   ---------------------

---- lua数据类型
print(type(7676))
print(type(print))
print(type(true))

tab1 = { key1 = 'val1', key2 = 'val2', 'val3'}
for k, v in pairs(tab1) do
    print(k .. '-' .. v)
end
-- lua循环
--[[
for var =exp1, exp2, exp3 do    exp3为步长
    <执行体>
end
]]--


for i=20, 1, -1 do
    print(i)
end


-- 将key1 设置为 nil
tab1.key1 = nil
for k, v in pairs(tab1) do
    print(k .. '=' .. v)
end

print('s' .. 'd') -- 拼接
length = 'www.baidu.com'
print(#length)   -- 计算长度

local tb1 = {}
local tb2 = {'aple', 'banana', c = 'orange', 'grape'}

for k , v in pairs(tb2) do
    print(k, v)
end

-- 函数
function func1(n)
    if n == 0 then
        return 1
    else
        return n * func1(n-1)
    end
end
print(func1(5))

function fun2(tab, fun)
    for k, v in pairs(tab) do
        print(fun(k, v))
    end
end

-- 流程控制
if(0)
then
    print('0 --> true')
end

-- 函数
function maximum(a)
    local mi = 1
    local m = a[mi]
    for i, val in ipairs(a) do
        if val > m then
            mi = i
            m = val
        end
    end
    return m, mi
end



function average(...) -- 利用select("#",...)获取可变参数的数量
    result = 0
    local arg = {...}
    for i, v in ipairs(arg) do
        result = result +v
    end
    print(select('#',...))
    return result/select('#',...)
end

print('均值为', average(10,2,4,3,4,2,1))

if (1 ~= 2) then
    print('asdf')
end

-- 字符串

print(string.upper('helloyou'))
print(string.gsub('aaaaabbb', 'b', 'c', 2))  -- 2为替换次数
print(string.reverse('Lua hello'))
print(string.len('aaaa'))
print(string.rep('abcd', 2)) -- 返回字符串string的n个拷贝
print('hello ' .. 'lua')

print(string.sub('hello lua', 2, 4))
print(string.sub('hello lua', -5))  -- 截取最后五个

print(string.format('hi %s %s', 'hello', 'lua'))
print(string.format('time is: %02d/%02d/%02d', 2, 1, 2022))
print(string.format('%05d', 23))

-- 数组
array = {'lua', 'tutorial'}    --一维数组
for i =0, 2 do
    print(array[i])
end

array = {}
for i=-2, 2 do
    array[i] = i*2
end

for i=-2,2 do
    print(array[i])
end

-- 初始化数组     三行三列的阵列多维数组
array = {}
for i=1,3 do
   array[i] = {}
      for j=1,3 do
         array[i][j] = i*j
      end
end

-- 访问数组
for i=1,3 do
   for j=1,3 do
      print(array[i][j])
   end
end

--迭代器
array = {'hi', 'mine'}   --泛型 for 迭代器
for k, v in pairs(array) do
    print(k,v)
end

-- lua 表
mytable = {}
print('mytable is ', type(mytable))
mytable[1] = 'hello'
mytable['wow'] = 'lua'