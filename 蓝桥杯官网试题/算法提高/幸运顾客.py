'''
为了吸引更多的顾客，某商场决定推行有奖抽彩活动。
“本商场每日将产生一名幸运顾客，凡购买30元以上商品者均有机会获得本商场提供的一份精美礼品。”
该商场的幸运顾客产生方式十分奇特：每位顾客可至抽奖台抽取一个幸运号码，该商场在抽奖活动推出的第i天将从所有顾客中（包括不在本日购物满30元者）挑出幸运号第i小的顾客作为当日的幸运顾客。
该商场的商品本就价廉物美，自从有奖活动推出后，顾客更是络绎不绝，因此急需你编写一个程序，为他解决幸运顾客的产生问题。

【输入数据】
　　第1行一个整数N，表示命令数。
　　第2~N+1行，每行一个数，表示命令。如果x>=0，表示有一顾客抽取了号码x；如果x=-1，表示傍晚抽取该日的幸运号码。
【输出数据】
　　对应各命令-1输出幸运号码；每行一个号码。(两个相同的幸运号看作两个号码)
样例输入
6
3
4
-1
-1
3
-1
样例输出
3
4
4
解释
　　只关注获奖的号码是多少，每个号码可以获奖多次
'''
n = int(input())

arr = []
rs = []

ans = 0

for i in range(n):
    data = int(input())
    if data != -1:
        arr.append(data)
    else:
        arr.sort()
        rs.append(arr[ans])
        ans += 1

for i in range(len(rs)):
    print(rs[i])
