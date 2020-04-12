'''
wlxsq决定制作一个Calc，该Calc具备求解一元一次方程的功能。

为了简化工作，拒绝花里胡哨。这个方程中，只有一个等号"="，零个或多个加号"+"、减号"-"，一种小写字母表示未知数。当然，减号也可是负号

方程中并没有括号，也没有除号，方程中的字母表示未知数。
输入
仅一行，表示一个合法的方程，包含“+”、“-”、“=”、数字及小写字母。

输出
仅一行，表示答案，形式为“未知元=答案”。对答案保留3位小数，保证答案的绝对值不超过10000。

样例

2a=1
a=0.500

-5+2x=-10
x=-2.500
'''
s=input()
x = ''
for i in s:
    if 97<=ord(i)<122:#取出未知数字母
        x=i
s=s.replace(x,'x')#把未知数字母替换成x
#表达式变形 如-5+2x=-10 -> -5+2*x-(-10)
s=s.replace('=','-(')+')'
s=s.replace('x','*x')
s=s.replace('+*x','+x')
s=s.replace('-*x','+x')
s=s.replace('(*x','(x')
#合并表达式，要用到复数,-5+2*x-(-10) -> (5+2j)
value=eval(s,{'x':1j})
# print(value)
# print(value.real) # 取实数部分
# print(value.imag) # 取复数部分
print('%s=%.3f'%(x,-value.real/value.imag))#5+2j=0,j就是未知数