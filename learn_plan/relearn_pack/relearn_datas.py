# 权重说明：
# 我的权重设置标准是，基准值：中等3分，容易2分，困难1分，如果带官方解答就在基准值上+1分
# 如果是面经上的经典算法，则按书上给的星级来给分
# 如果是实验楼的课程，那么挑战5分，实验4分

# 经典算法
CL = {
        '快速排序':5,
        '堆排序':4,
        '冒泡排序':4,
        '归并排序':4,
        '插入排序':3,
        '希尔排序':3,
        '基数排序':3,
        '选择排序':2,
}

# 要付费的题
LC_PAY = {
        'LC272':1,
}

# 不是算法题
LC_NOT_ALG = {
        'LC178':3,
}

# LeetCode算法
LC_ACed = {
        'LC877':4,
        'LC338':3,
        'LC563':3,
        'LC680':3,
        'LC810':2,
        'LC83':3,
        'LC698':4,
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
        'LC575':3,
        'LC944':3,
        'LC855':4,
}

algorithms = {}
algorithms.update(LC_ACed)
algorithms.update(CL)

# 自动生成楼+实验号
SY = {f'实验{x}':4 for x in range(3,21)}

# 自动生成楼+挑战号
TZ = {f'挑战{x}':5 for x in range(1,23)}

# 普通实验列表
# 楼＋课程有点根本顾不过来，普通实验就不再设置复习了
# 但做过的实验一定要写在里面
# LS = {
#         'Python设计模式':3,
#         'NumPy使用教程 1':3,
#         'NumPy使用教程 2':3,
#         'NumPy使用教程 3':3,
#         'NumPy使用教程 4':3,
#         'Pandas使用教程 1':3,
# }

shiyanlou = {}
shiyanlou.update(SY)
shiyanlou.update(TZ)
# shiyanlou.update(LS)

# 把所有字典合起来
TOTAL = {}
TOTAL.update(CL)
TOTAL.update(LC_ACed)
TOTAL.update(SY)
TOTAL.update(TZ)
# TOTAL.update(LS)
