import sys


LOW = 0
HIGH = 1
RATE = 2
FAST = 3
table = [
    [0, 3000, 0.03, 0],
    [3000, 12000, 0.1, 210],
    [12000, 25000, 0.2, 1410],
    [25000, 35000, 0.25, 2660],
    [35000, 55000, 0.3, 4410],
    [55000, 80000, 0.35, 7160],
    [80000, None, 0.45, 15160],
]
insure = {
    'old':0.08,
    'med':0.02,
    'lost':0.005,
    'injure':0,
    'child':0,
    'house':0.06
}

def cal_cash(income):
    try:
        income = int(income)
    except ValueError:
        print("Parameter Error")
    insure = should_insure(income)
    tax = should_tax(income, insure)
    return "{:.2f}".format(income - insure - tax)

def should_insure(income):
    result = 0
    for i in insure:
        result += income * insure.get(i)
    return result

def should_tax(income, insure):
    result = income - 5000 - insure

    if result <= 0:
        return 0
    for i in table:
        if result > i[LOW] and \
            (result <= i[HIGH] or i[HIGH] == None):
            return result * i[RATE] - i[FAST]

if __name__ == '__main__':
    for i in sys.argv[1:]:
        the_id, the_salary = i.split(':')
        print(the_id + ':' + cal_cash(the_salary))

