'''
生成每日学习计划（楼+没课的日子）
如果有付费题或者非算法题，加入相关数据集，今天就少做这些题
如果全是付费题或者非算法题，你的重点就应该是复习
每做完一题不要忘记更新做题数据
# 楼+的实验和挑战都比较花时间
# 有没搞定的就光做没搞定的，都搞定了就随机挑几个复习
# 只把学过的普通课和会员课加入数据集，不复习，时间真的不够
'''

from relearn_pack import new_lc_list, relearn_list, algorithms, shiyanlou, STATUSES

STATUS = STATUSES['default']

if STATUS['new']:
    print('==========今日新题==========')
    for x in new_lc_list(STATUS['new']):
        print(x)

if STATUS['reform']:
    print('==========今日复习==========')
    for x in relearn_list(algorithms, STATUS['reform']):
        print(x)
    
if STATUS['louplus']:
    print('==========楼+复习==========')
    for x in relearn_list(shiyanlou, STATUS['louplus']):
        print(x)

