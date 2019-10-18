# _*_ coding:UTF8 _*_
"""
① Pythonのバージョン確認、モジュールのimport、データの読み込み
"""
# Imports

# pandas
import pandas as pd
from pandas import Series, DataFrame

# numpy, matplotlib, seaborn
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

# get titanic & test csv files as a DataFrame
titanic_df = pd.read_csv(
    r"C:\work\developer\PycharmProjects\myDemo\DataAnalysis\data\train.csv",
    encoding='utf-8')
"""
② 簡単にデータの状態を確認する（行数列数カウント・データの選択的表示・重複の有無など）
"""

# preview the data
# データの確認をする（最初の3行を表示）
titanic_df.head(3)

# 先頭の5行を表示
titanic_df.head()

# 最後尾の5行を表示
titanic_df.tail()

# 簡単にデータの状態を確認する（行数列数カウント・データの選択的表示・重複の有無など）
print('dataframeの行数・列数の確認==>\n', titanic_df.shape)
print('indexの確認==>\n', titanic_df.index)
print('columnの確認==>\n', titanic_df.columns)
print('dataframeの各列のデータ型を確認==>\n', titanic_df.dtypes)

print(100 * '#')

# 任意の列だけ取り出したい場合
titanic_df[['Name', 'Age']].head

print(100 * '#')

# 100行目から105行目まで表示したい場合
titanic_df[100:106]

print(100 * '#')
# indexが100の行だけ取得したい場合
titanic_df.loc[100]

# もっとピンポイントに抽出したい場合
# 例：1,2,4　行目と0-2列目を取得
titanic_df.iloc[[1, 2, 4], [0, 2]]

# 条件を指定して抽出
titanic_df[titanic_df['Age'] >= 35]

# queryメソッドを使うと、複数条件の指定で、特定カラムだけ出力もできる
titanic_df[['Name', 'Age']].query('Age >= 35 and Name.str.contains("Miss")',
                                  engine='python')

# 'Cabin'には例えばどんなデータが入っているか確認
titanic_df['Cabin'].unique()

# Cabin単位で重複したデータが存在しないか確認
print(len(titanic_df) == len(titanic_df['Cabin'].unique()))

# 行方向で重複行を削除
titanic_df.drop_duplicates()
# 重複が存在しないので数は変わらないはず
print(titanic_df.shape)

# 要約統計量の表示
# include:默认只输出数值型数据的统计信息(如上),设置参数为'all'则输入的所有列都在输出中,设置为O则只输出离散型变量的统计信息
# eg:df.describe(include='all')
# eg:df.describe(include='O')
titanic_df.describe()

# 观察数据 和 数据类型
titanic_df.info()
"""
③ データの整形（データ型変更、列名変更、並び替えなど）
"""

# Name列をindexにする
# titanic_df.set('Name', inplace=True)

# カラム名を変更する（Name を Full Name に変換）
df_org = titanic_df.copy()
df_org.rename(columns={'Name': 'Full Name'}, inplace=True)
df_org.head(3)

# 臨時テストデータ用
list_l = [[1, 3, 3, 5, 4], [11, 7, 15, 13, 9], [4, 2, 7, 9, 3],
          [15, 11, 12, 6, 11]]
index = ["2018-07-01", "2018-07-02", "2018-07-03", "2018-07-04"]
df = pd.DataFrame(list_l, index=index, columns=['a', 'b', 'c', 'd', 'e'])
df.head()

# カラム名を変更する（Name を Full Name に変換）
df_rename = df.rename({'a': 'A'}, axis='columns')
df_rename.head()

# https://vimsky.com/article/3838.html
# set_index reset_index
# set_index 本身会生成一个新的df 如果设定 inplace=True 会改变既有的df的结构
print(df_rename.index)
indexed1 = df_rename.set_index('A', inplace=True)
print(indexed1)
df_rename.head()

# set_index 本身会生成一个新的df 如果不设定 inplace=True bu会改变既有的df的结构
indexed2 = df_rename.set_index(['b', 'c'])
print(indexed2)
indexed2.head()
df_rename.head()

# http://www.voidcn.com/article/p-zqcfzovw-byr.html
# 作用：reset_index可以还原索引为普通列，重新变为默认的整型索引
# df_rename.reset_index()

# 多级索引
index = pd.MultiIndex.from_product([['TX', 'FL', 'CA'], ['North', 'South']],
                                   names=['State', 'Direction'])
df = pd.DataFrame(index=index,
                  data=numpy.random.randint(0, 10, (6, 4)),
                  columns=list('abcd'))
df.head()

# 'Cabin'列を降順で並び替えもできる
titanic_df.sort_values(by='Cabin', ascending=True).head()

# sort_valuesは複数の列に対しても実行できる
titanic_df.sort_values(['Cabin', 'Sex'], ascending=True).head()

# テストデータ日付を含む
lunch_df = pd.read_csv(
    r"C:\work\developer\PycharmProjects\myDemo\DataAnalysis\data\lunch_box.csv",
    encoding='utf-8')
lunch_df.head()

print('dataframeの行数・列数の確認==>\n', lunch_df.shape)
print('indexの確認==>\n', lunch_df.index)
print('columnの確認==>\n', lunch_df.columns)
print('dataframeの各列のデータ型を確認==>\n', lunch_df.dtypes)

# datetime列をindexにする
lunch_df.set_index('datetime', inplace=True)
lunch_df.head()

# カラム名を変更する（y を sales に変換）
lunch_df.rename(columns={'y': 'sales'}, inplace=True)
lunch_df.head()

# 'sales'列を降順で並び替えもできる
lunch_df.sort_values(by="sales", ascending=True).head()  # ascending=Trueで昇順

# sort_valuesは複数の列に対しても実行できる
lunch_df.sort_values(['sales', 'temperature'],
                     ascending=False).head()  # ascending=Falseで昇順

# indexのデータ型を確認してみる
lunch_df.index

# indexであるdatetimeのdtype='object' を dtype='datetime64[ns]' に変更
lunch_df.index = pd.to_datetime(lunch_df.index, format='%Y-%m-%d')

# indexのデータ型を確認してみる
lunch_df.index
