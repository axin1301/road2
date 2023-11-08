import pandas as pd
import os

df_all = pd.DataFrame({})
for year in [2017,2021]:
    for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian']:#,'linquanxian','jingyuxian','lingqiuxian']:
        if os.path.exists('../output/'+county+'_'+str(year)+'_d500_recall.csv'):
            df = pd.read_csv('../output/'+county+'_'+str(year)+'_d500_recall.csv')
            df_all = pd.concat([df_all, df])
df_all.to_csv('validation_statistics_first10_d500_recall.csv', index=False)

df_all = pd.DataFrame({})
for year in [2017,2021]:
    for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian']:#,'linquanxian','jingyuxian','lingqiuxian']:
        if os.path.exists('../output/'+county+'_'+str(year)+'_OSM_recall.csv'):
            df = pd.read_csv('../output/'+county+'_'+str(year)+'_OSM_recall.csv')
            df_all = pd.concat([df_all, df])
df_all.to_csv('validation_statistics_first10_OSM_recall.csv', index=False)

df_all = pd.DataFrame({})
for year in [2017,2021]:
    for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian']:#,'linquanxian','jingyuxian','lingqiuxian']:
        if os.path.exists('../output/'+county+'_'+str(year)+'_b1_recall.csv'):
            df = pd.read_csv('../output/'+county+'_'+str(year)+'_b1_recall.csv')
            df_all = pd.concat([df_all, df])
df_all.to_csv('validation_statistics_first10_b1_recall.csv', index=False)

df_all = pd.DataFrame({})
for year in [2017,2021]:
    for county in ['shufuxian','xixiangxian','guanghexian','danfengxian','jiangzixian','honghexian','liboxian']:#,'linquanxian','jingyuxian','lingqiuxian']:
        if os.path.exists('../output/'+county+'_'+str(year)+'_b2_recall.csv'):
            df = pd.read_csv('../output/'+county+'_'+str(year)+'_b2_recall.csv')
            df_all = pd.concat([df_all, df])
df_all.to_csv('validation_statistics_first10_b2_recall.csv', index=False)


data = pd.read_csv('validation_statistics_first10_d500_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': x['pre'].mean(),  # 计算 pre 值
    'rec': x['rec'].mean(),  # 计算 rec 值
    'f1s': x['f1s'].mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_d500_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名



data = pd.read_csv('validation_statistics_first10_OSM_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby([ 'roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': x['pre'].mean(),  # 计算 pre 值
    'rec': x['rec'].mean(),  # 计算 rec 值
    'f1s': x['f1s'].mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_OSM_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名



data = pd.read_csv('validation_statistics_first10_b1_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': x['pre'].mean(),  # 计算 pre 值
    'rec': x['rec'].mean(),  # 计算 rec 值
    'f1s': x['f1s'].mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_b1_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名



data = pd.read_csv('validation_statistics_first10_b2_recall.csv')
# 按照指定列进行分组，计算每组的 pre, rec, f1s 值
grouped = data.groupby(['roadclass', 'year', 'i']).apply(lambda x: pd.Series({
    'pre': x['pre'].mean(),  # 计算 pre 值
    'rec': x['rec'].mean(),  # 计算 rec 值
    'f1s': x['f1s'].mean()  # 计算 f1s 值
}))

# 重置索引
grouped = grouped.reset_index()

# 保存结果为新的 CSV 文件
grouped.to_csv('validation_statistics_first10_b2_recall_grouped.csv', index=False)  # 保存为 result_grouped.csv，可以根据需要修改文件名