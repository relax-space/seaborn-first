import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def bar_1():
    # 对数据分组 排序,并计算每组的数量
    data = [2, 3, 4, 5, 1, 6, 5, 5, 4, 4, 4, 4, 3, 2]
    sns.histplot(data=data, bins=3)
    plt.show()
    pass


def bar_2(df: pd.DataFrame):
    # 按照flipper_length_mm列 里面的数据分组,并计算每组的数量
    sns.histplot(data=df, bins=3)
    plt.show()
    pass


def bar_3(df: pd.DataFrame):
    '''
    shrink: 直方图间距
    hue: 分组
    multiple可选参数：
        layer:分层（默认）
        dodge:并排
        stack堆叠
        fill:填充
    col: 分面, 这个要调用displot方法,而不是histplot,但是我会闪退 col='sex'
    '''
    # layer 和stack的区别,第一个会重叠, 第二个没有重叠的部分
    sns.histplot(
        data=df,
        x='flipper_length_mm',
        shrink=0.5,
        hue='species',
        multiple='dodge',
    )
    plt.show()


def main(df: pd.DataFrame):
    bar_1()
    bar_2(df)
    bar_3(df)


if __name__ == '__main__':
    df = pd.read_csv('data/penguins.csv')
    main(df)
    pass
