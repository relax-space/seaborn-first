'''
说明: 主要解释y轴数据的由来: 据说是等差分组,然后计算每组的数量,结果证明确实是这样

注:因为不知道怎么获取sns.histplot的返回值,所以用plt.hist
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def calc_count(x1, x2, data: list):
    count = 0
    for i in data:
        if i >= x1 and i < x2:
            count += 1
    return count


def valid_1():
    a1: list = [2, 3, 4, 5, 1, 6, 5, 5, 4, 4, 4, 4, 3, 2, 3.5]
    # 1. 显示2个轴, bins: 表示轴的数量
    bins = 2
    ax = plt.hist(a1, bins=bins)
    print(ax)

    # 2. 打印信息: ax打印出来的值 (array([ 5., 10.]), array([1. , 3.5, 6. ]), <BarContainer object of 2 artists>)
    '''
    分析: 
        1. 等差: x坐标上的2个轴需要3个数据做标记,所以ax[1]就是把1到6分成距离相等的3个数字
        2. 获取分组的数量: 比如1~3.5之间有多少数据,前开后闭, 但是如果是最后一个数字必须带上
    '''
    exp = np.linspace(min(a1), max(a1), num=(bins + 1))
    ax2 = ax[1]
    assert ax2.tolist() == exp.tolist(), 'linspace error'

    exp = ax[0]
    act = []
    ax2_len = len(ax2)
    for k in range(ax2_len):
        number = calc_count(ax2[k], ax2[k + 1], a1)
        act.append(number)
        if k + 1 == ax2_len - 1:
            # 最后一个轴的处理
            act[-1] = act[-1] + 1
            break
    assert exp.tolist() == act, 'number error'
    plt.show()


def valid_2(df):
    # 1. 显示2个轴, bins: 表示轴的数量
    bins = 2
    s1: pd.Series = df['flipper_length_mm']
    ax = plt.hist(s1, bins=bins)
    print(ax)

    # 2. 打印信息: ax打印出来的值 (array([200., 142.]), array([172. , 201.5, 231. ]), <BarContainer object of 2 artists>)
    '''
    分析: 
        1. 等差: x坐标上的2个轴需要3个数据做标记,所以ax[1]就是把172到231分成距离相等的3个数字
        2. 获取分组的数量: 比如172~201.5之间有多少数据
    '''
    exp = np.linspace(s1.min(), s1.max(), num=(bins + 1))
    ax2 = ax[1]
    assert ax2.tolist() == exp.tolist(), 'linspace error'

    exp = ax[0]
    act = []
    ax2_len = len(ax2)
    for k in range(ax2_len):
        number = calc_count(ax2[k], ax2[k + 1], s1.values.tolist())
        act.append(number)
        if k + 1 == ax2_len - 1:
            # 最后一个轴的处理
            act[-1] = act[-1] + 1
            break
    assert exp.tolist() == act, 'number error'
    plt.show()


def main():
    valid_1()
    df = pd.read_csv('data/penguins.csv')
    valid_2(df)


if __name__ == '__main__':
    main()
