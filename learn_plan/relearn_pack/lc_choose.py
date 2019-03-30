from random import choice, randint

def new_lc_list(total_nums=10, TOTAL=1023):
    # TOTAL是指LeetCode一共有多少题，默认值常变
    from .relearn_datas import LC_ACed, LC_PAY, LC_NOT_ALG
    results = []
    choice_times = 0
    while len(results) < total_nums:
        choice_times += 1
        if choice_times > TOTAL:
            print('你已经刷完新题了')
            return
        x = randint(1, TOTAL+1)
        if 'LC'+str(x) not in LC_ACed \
        and 'LC'+str(x) not in LC_PAY \
        and 'LC'+str(x) not in LC_NOT_ALG:
            results.append(x)
    return results

def relearn_list(datas, nums=10):
    # datas是带权重的键值对，详见relearn_datas
    table = []
    for i in datas:
        for _ in range(datas[i]**2):
            table.append(i)
    
    result = []
    while len(result) < nums:
        rand_item = choice(table)
        if rand_item not in result:
            result.append(rand_item)
    
    return result