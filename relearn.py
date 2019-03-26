'''
需要复习，但是却无从下手的时候，运行这个
由于KL这个字典的特殊性，规定：
经典算法与数据结构从顶部加入
LeetCode题从底部加入
并且每做一道题就要添加一次
否则等着混乱吧……
实在要是混乱了，就用bs4来解析一下静态页面好了，那样需要维护的就只有经典题了
'''

# 上：经典算法；下：LeetCode算法
KL = {
        '快速排序':5,
        '堆排序':4,
        '冒泡排序':4,
        '归并排序':4,
        '插入排序':3,
        '希尔排序':3,
        '基数排序':3,
        '选择排序':2,
        'LC981':4,
        'LC922':3,
        'LC852':3,
        'LC778':2,
        'LC744':3,
        'LC739':4,
        'LC718':4,
        'LC658':4,
        'LC387':3,
        'LC374':3,
        'LC349':3,
        'LC287':4,
        'LC278':3,
        'LC236':4,
        'LC206':3,
        'LC189':3,
        'LC167':3,
        'LC162':4,
        'LC153':4,
        'LC145':2,
        'LC144':4,
        'LC136':3,
        'LC112':3,
        'LC105':4,
        'LC104':3,
        'LC102':4,
        'LC101':3,
        'LC98':4,
        'LC94':4,
        'LC50':4,
        'LC34':4,
        'LC33':4,
        'LC21':3,
        'LC20':3,
        'LC1':3,
        'LC707':2,
        'LC704':2,
        'LC454':3,
        'LC392':3,
        'LC378':3,
        'LC367':2,
        'LC350':2,
        'LC344':2,
        'LC234':2,
        'LC230':3,
        'LC155':2,
        'LC150':3,
        'LC117':3,
        'LC116':3,
        'LC108':2,
        'LC106':3,
        'LC69':2,
        'LC28':2,
        'LC24':3,
        'LC8':3,
        'LC973':4,
        'LC969':4,
}

# 自动生成楼+实验号
SY = {f'实验{x}':4 for x in range(3,21)}

# 自动生成楼+挑战号
TZ = {f'挑战{x}':5 for x in range(1,19)}

# 普通实验列表
LS = {
        'Python设计模式':3,
        'NumPy使用教程 1':3,
        'NumPy使用教程 2':3,
        'NumPy使用教程 3':3,
        'NumPy使用教程 4':3,
}

# 把所有字典合起来
TOTAL = {}
TOTAL.update(KL)
TOTAL.update(SY)
TOTAL.update(TZ)
TOTAL.update(LS)

weight_top = 10
weight_count = 0
result = []

from random import choice
table = []
for i in TOTAL:
    for _ in range(TOTAL[i]**2):
        table.append(i)

while weight_count < weight_top:
    rand_item = choice(table)
    if rand_item not in result:
        result.append(rand_item)
        weight_count += TOTAL[rand_item]

for x in result:
    print(x)

