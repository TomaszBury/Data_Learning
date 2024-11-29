data_url = 'https://gist.githubusercontent.com/sh7ata/56976975b3c67caabb2efd80bb3a8467/raw/f1b7d2abf6770548edafee58ea15be71e2d28aac/Nutrition.csv'

data_url = 'https://andybek.com/pandas-soccer'

df.rename(columns={'wieght':'Weight (kg)'}, index={0:'Pikachu',1:'Andy'}, inplace=True)

df.rename(mapper={'height': 'Height (m)'},axis='columns')

**dfm.replace(to_replace='\sg', value='', regex=True)**

df.dropna(thresh=df.shape[1], axis=1)

players.loc[players.age.le(25)] == players.loc[players.age <= 25]

<  .lt()
<= .le()
>  .gt()
>= .ge()
== .eq()

data_url = 'https://andybek.com/pandas-soccer'

players.reindex(index=index_players, columns=sorted(players.columns))

unwanted_columns = ['name', 'position', 'position_cat']

players.reindex(columns=set(players.columns).difference(unwanted_rows))


unwanted_rows = [1,2,3,4]

players.reindex(index=set(players.index).difference(unwanted_rows))

players.loc[players.isna().values].drop_duplicates()

df2.nationality.nunique()

df2 = players.drop(index=[2,10,21], columns='market_value')

players.select_dtypes(np.number).agg(['min','max','mean'])

def random_case(x):

    funcs = [x.str.swapcase, x.str.lower, x.str.title, x.str.upper]
    
    return choice(funcs)()

players.loc[460, [dtype != object for dtype in players.dtypes]]

## at[] and iat[] should be preferred for single value assignment

## df_mini.insert(0, 'nicknames', players_names)

df_mini.assign(career_goals=[12,67,179,49])

pd.concat(dfs, ignore_index=True).drop_duplicates(subset=['School Name'])

pd.concat([ivies, eng4], join='inner', ignore_index=True, verify_integrity=True)

pd.merge(ivies, regions, how='inner', on='School Name')

# 180. - The anatomy of a multiindex object

tech.index.names

tech.index.levels

**tech.index.nlevels**

tech.index.levels[0]

tech.index.levshape

tech.reorder_levels([2,1,0])

tech.reset_index(level=['date','name'], drop=False)

tech.sort_index(inplace=True)

tidx.is_monotonic_increasing

tidx.sortlevel(0,ascending=False, sort_remaining=True)

tidx.sortlevel((0,1,2), ascending=[False,True,False])

tidx.set_names(['Treading Date','Volume Category','Ticker'], inplace=True)

tidx.to_flat_index()

tech.stack()

stacked.unstack(level='Ticker', fill_value='-')

**tech.describe()**

platform_names = {
    'PS3':'PlayStation',
    'PS4':'PlayStation',
    'X360':'XBox',
    'XOne':'XBox'
}

sales.set_index('Platform').groupby(platform_names).sum()

sales.groupby('Platform').get_group('PS3')

studios.groupby(studios_groupby).agg(['sum','mean','std','count'])

studios.groupby(studios_groupby).agg(studios_aggregation).rename({'sum':'Total_revenue','count':'number_games'},axis=1)

studios.groupby(studios_groupby).agg(
    Total_revenue=('Global_Sales','sum'), 
    Number_of_games=('Global_Sales',np.mean),
    Revenue_std=('Global_Sales','std'),
    Revenue_avg=('Global_Sales','mean'))

# Running cells with 'Python 3.11.0 64-bit' requires ipykernel package.
# Run the following command to install 'ipykernel' into the Python environment. 
# Command: 'python.exe -m pip install ipykernel -U --user --force-reinstall'

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# It is alive!