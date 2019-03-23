#!/usr/bin/env python3

import csv, sys


class SalaryCalculator(object):
    '''
    -c : insure config path
    -d : the raw income file
    -o : the output path
    '''

    def __init__(self):
        self.TAX_TABLE = [
            [0, 3000, 0.03, 0],
            [3000, 12000, 0.1, 210],
            [12000, 25000, 0.2, 1410],
            [25000, 35000, 0.25, 2660],
            [35000, 55000, 0.3, 4410],
            [55000, 80000, 0.35, 7160],
            [80000, None, 0.45, 15160],
        ]

        self.SOCIAL_INSURE_FILE = ""
        self.USER_RAW_INCOME_FILE = ""
        self.PATH_EXPORT = ''
        args = sys.argv[1::2]
        paths = sys.argv[2::2]
        args_length = len(args)
        args_paths = {}
        for i in range(0, args_length):
            args_paths[args[i]] = paths[i]
        for i in args_paths:
            try:
                self.parse_option(i, args_paths[i])
            except:
                print('Some Error.Please check options.')

        with open(self.SOCIAL_INSURE_FILE) as cfgf:
            tmpd = {}
            tmps = cfgf.readlines()
            for i in tmps:
                print(i.split(' = '))
                k, v = i.split(' = ')
                tmpd[k] = float(v)
            self.social_insure = tmpd
        with open(self.USER_RAW_INCOME_FILE) as csvf:
            self.user_income = list(csv.reader(csvf))
        for i in self.user_income:
            i[1] = float(i[1])

    def show_cfg_content(self):
        '''
        test from eyes
        '''
        print(self.social_insure)
        print(self.user_income)
        for i in self.user_income:
            print('{}--baseline:{}|should insure:{}|should tax:{}'.format(i[0],
                self.insure_baseline(i[1]),
                self.get_insure(self.insure_baseline(i[1])),
                self.get_tax(i[1] - self.get_insure(self.insure_baseline(i[1])))
            ))
        print('all result:')
        for i in self.calculate_cash():
            print(i)


    def insure_baseline(self, income):
        if income > self.social_insure['JiShuH']:
            return self.social_insure['JiShuH']
        elif income < self.social_insure['JiShuL']:
            return self.social_insure['JiShuL']
        else:
            return income

    def get_insure(self, income):
        insure_rate = self.social_insure['YangLao'] + \
            self.social_insure['YiLiao'] + \
            self.social_insure['ShiYe'] + \
            self.social_insure['GongShang'] + \
            self.social_insure['ShengYu'] + \
            self.social_insure['GongJiJin']
        return self.insure_baseline(income) * insure_rate

    def get_tax(self, pretax):
        low = 0
        high = 1
        rate = 2
        fast = 3
        prepare = pretax - 5000

        if prepare <= 0:
            return 0
        for i in self.TAX_TABLE:
            if prepare > i[low] and \
                (prepare <= i[high] or i[high] == None):
                return prepare * i[rate] - i[fast]

    def calculate_cash(self):
        result = []
        for i in self.user_income:
            item = [i[0]]
            insure = self.get_insure(i[1])
            tax = self.get_tax(i[1] - insure)
            item.append(int(i[1]))
            item.append('{:.2f}'.format(insure))
            item.append('{:.2f}'.format(tax))
            item.append('{:.2f}'.format(i[1] - insure - tax))
            result.append(item)
            # print(item)
        return result

    def export(self):
        with open(self.PATH_EXPORT, 'w') as f:
            csv.writer(f).writerows(self.calculate_cash())

    def parse_option(self, option, target):
        if option == '-c':
            self.SOCIAL_INSURE_FILE = target
        elif option == '-d':
            self.USER_RAW_INCOME_FILE = target
        elif option == '-o':
            self.PATH_EXPORT = target
        else:
            raise


if __name__ == '__main__':

    calculator = SalaryCalculator()
    calculator.export()
