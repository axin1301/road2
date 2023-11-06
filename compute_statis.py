import pandas as pd

data = pd.read_csv('validation_statistics_first10_d500_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['county', 'roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': (x['pre'] * x['count']).sum() / x['count'].sum(),  # 计算 pre 值
    'rec': (x['rec'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    'f1s': (x['f1s'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    # 'f1s': (2 * (x['pre'] * x['rec']) / (x['pre'] + x['rec'])).mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_d500_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名



data = pd.read_csv('validation_statistics_first10_OSM_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['county', 'roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': (x['pre'] * x['count']).sum() / x['count'].sum(),  # 计算 pre 值
    'rec': (x['rec'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    'f1s': (x['f1s'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    # 'f1s': (2 * (x['pre'] * x['rec']) / (x['pre'] + x['rec'])).mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_OSM_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名



data = pd.read_csv('validation_statistics_first10_b1_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['county', 'roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': (x['pre'] * x['count']).sum() / x['count'].sum(),  # 计算 pre 值
    'rec': (x['rec'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    'f1s': (x['f1s'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    # 'f1s': (2 * (x['pre'] * x['rec']) / (x['pre'] + x['rec'])).mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_b1_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名



data = pd.read_csv('validation_statistics_first10_b2_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['county', 'roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': (x['pre'] * x['count']).sum() / x['count'].sum(),  # 计算 pre 值
    'rec': (x['rec'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    'f1s': (x['f1s'] * x['count']).sum() / x['count'].sum(),  # 计算 rec 值
    # 'f1s': (2 * (x['pre'] * x['rec']) / (x['pre'] + x['rec'])).mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_b2_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名