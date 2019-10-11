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
    r"C:\work\developer\PycharmProjects\myDemo\DataAnalysis\train.csv",
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
titanic_df.rename(columns={'Name', 'Full Name'}, axis='columns')
