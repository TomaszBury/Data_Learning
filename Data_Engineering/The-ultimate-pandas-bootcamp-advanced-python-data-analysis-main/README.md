### The-ultimate-pandas-bootcamp-advanced-python-data-analysis
 https://nordea.udemy.com/course/the-ultimate-pandas-bootcamp-advanced-python-data-analysis/


### 25

iloc => integer loc => indexing by position
loc => location => indexing by label

### 26 - Using Callables with .loc and .iloc

lambda <-- anonimus function https://www.programiz.com/python-programming/anonymous-function

### 27 Seleting with .get()

### 28 Selection Recap

### 29 Skill challenge

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.equals.html

### 30 solutions

### 33 Reading data from csv

### 34 Series Sizing With .size .shape ANd len()

https://www.programiz.com/python-programming/methods/list/reverse

https://pbpython.com/pandas_dtypes.html

### 36 count() method

### 37 Accessing and counting NA's

### Pandorable <-- adorable and involving pandas

alcohol.isna().sum() == alcohol.isnull().sum()

### 38 BONUS: Another Approach

### 39 The Other Side: notnull() and notna()

### 40 BONSU: Booleans are literally number in Python

### 41 Skill Challenge

### 43 Dropping and filling NAs

### 44 Descriptice statistic

https://en.wikipedia.org/wiki/Quantile

alcohol.describe()

### 45 Describe() Method

from math import sqrt
sqrt()

### 46 mode() and value_counts()

alcohol.value_counts(normalize=True).head(n=17)

### 47: idxmax() & idxmin()

### 48 Sorting with sort_values()

alcohol.sort_values(ascending=False, na_position='first')

**alcohol.sort_values(ascending=False, na_position='last', kind='quicksort').head(n=1) <-- best one**

alcohol.sort_values(ascending=False, na_position='first', kind='mergesort').head(n=1)

alcohol.sort_values(ascending=False, na_position='first', kind='heapsort').head(n=3)

### 49 nlargest() and nsmallest()

### 50 Sorting with sort_index()

# 51 Skill Challenge

## 52 Solution

### 53 basic math Series arithmetics and fill_value()

### 54 Bonus: Calculating Varaince and Standard Deviation

### 55 Cumulative Operations 

sum()

alcohol.cumsum()

alcohol.cumprod()

### 56 Pairwise Differences with diff()

### 57 Iteration Series

for i, v in mini_alc.items():
    print(f'Index:{i}, value:{v}')

### 58 Filtering: filter(), where(), and mask()

### filter on index:

alcohol.filter(regex='^V') 

alcohol.filter(like='stan') **<- like in SQL>**

### fileter on values:

alcohol.get(alcohol > 200)

def gt200(x): return x > 200

alcohol[gt200]

### replace with corresponding value when condition is FALSE

alcohol.where(lambda x: x > 200, other='Too small.')

alcohol.where(lambda x:x>200, other=pd.NA) <-default  NaN>

alcohol.where(lambda x:x>200).dropna()

### replace with corresponding value when condition is TRUE

alcohol.where(lambda x:x<=200).dropna()

alcohol.mask(lambda x:x>200).dropna()

### 59 Transforming with update(), apply(), map()

### Spot change

alcohol.update(pd.Series(data=[200,20], index=['Albania','Andorra']))

### global change

alcohol.apply(lambda x:x**2)

alcohol.apply(np.square) <-vectorized operations >

https://www.pythonlikeyoumeanit.com/Module3_IntroducingNumpy/VectorizedOperations.html

def multiply_by_self(x): return x*x

alcohol.apply(multiply_by_self)

### substituting each values in a Series with another values

### in siple transformations apply & map is the same for more advanced transformation use apply

### 60 Sill Challenge

pip install scipy

https://stackoverflow.com/questions/24761998/pandas-compute-z-score-for-all-columns

https://pandas.pydata.org/docs/user_guide/visualization.html

### 67 Creating a DataFrame

### **ValueError: All arrays must be of the same length**

### 68 in 67.file Bonus - Four more ways to build DataFrames

The enumerate function

ZIP
### 69 

### 70 

data_url = 'https://gist.githubusercontent.com/sh7ata/56976975b3c67caabb2efd80bb3a8467/raw/f1b7d2abf6770548edafee58ea15be71e2d28aac/Nutrition.csv'

### 71 DataFrames

### 72 Sample() method

nutrition.sample(frac=0.01) <-- fraction of data>

### 73 Bonus - sapling with replacement or weights

### 74 BONUS - How are random numbers generated

https://www.random.org

https://en.wikipedia.org/wiki/Mersenne_Twister

### 75 DataFrames Axes

nutrition.axis

nutrition.columns

nutrition.index

### nutrition.dropna(axis=)
### 0 == rows
### 1 == columns

### 76 Changing the index

nutrition.set_index('folic_acid', drop=False, append=True, verify_integrity=False, inplace=True)

nutrition.index = pd.RangeIndex(start=0, stop=8789, step=1)

### 77 Extracting from DataFram by Label

nutrition.loc['Eggplant, raw', 'calories']

nutrition.loc['Eggplant, raw']['calories']

nutrition.loc['Eggplant, raw':'Sherbet, orange', 'calories':'cholesterol']

nutrition.iloc[2:4,5:6]

nutrition.loc[['Raspberries, raw'],['protein','vitamin_b6']]

nutrition.loc[
    ['Raspberries, raw', 'Blackberries, raw'],
    ['protein','vitamin_b6','water']
]

### 78 DataFrame Extraction by Position

nutrition.iloc[[4,5,6],:] <- select all columns>

### 79 Single Value Access With .at and .iat

%timtimeit

### 80 BONUS - The get_loc() Method

### 81 Skill challenge

### 82 Sollution

### 83 Start of cleanup: Going Numeric

### 84 The astype() method

### 85 DataFrame replace() + A Flimpse at Regex

dfm.replace(to_replace='100 g',value=100)

regex -> regular expressions **https://regex101.com**

**dfm.replace(to_replace='\sg', value='', regex=True)**

### 86 Part I: Collecting the Units

### 87  The raname() method

df.rename(columns={'wieght':'Weight (kg)'}, index={0:'Pikachu',1:'Andy'}, inplace=True)

df.rename(mapper={'height': 'Height (m)'},axis='columns')

### 88 DataFrame dropna()

df.dropna(how='any',axis=0)

df.dropna(how='all', axis=0)

df.dropna(thresh=3, axis=0)

df.dropna(thresh=df.shape[1], axis=1)

### 89 BONUS dropna()

### 89 Part II Merging Units with column names

### 90

### 91 Part III Removing units fro mvalues

### 92 Filtering in 2D

### 93 Data Frame sorting

### 94 Using Series between() with DataFrames

### 95 Min, Max and idx[MinMax]

### 96 

### 97 DataFrame nlargest() and nsmallest()

# 98 Skill challenge

## 99 Solution

# 100 Skill challenge

## 101 Solution

### 102 Section recap notebook

### 103 Section intro

### 104 Intrducing a new dataset

### 105 Quick review: indexing with boolean masks

### 106 More approaches to boolean masking

### 107 Binary operators with booleans

### 108 BONUS - XOR and Complement Binary Ops

### 109 Combining Conditions

### 110 Conditions as Variables

# 111 Skill challenge

## 112 Solution

### 113 2d indexing

### 114

### 115 Sorting by index or columns

### 116 Sorting vs Reordering

### 117 BONUS - Another Way

### 118 BONUS Please Avoid Sorting like this

# 119 Skill Challenge

## 120 Solution

### 121 indentifying duplicates

### 122 removing duplicates

### 123 Removing DataFrame Rows

### 124 BONUS - Removing Columns

### 125 BOUNS - Another way: pop()

### 126 BONUS - A sophisticated alternative

### 127 NULL values in data frames

### 128 Dropping and filling DataFrame NAs

### 129 BONUS - Methods and Axes with fillna()

# 130 Skill Challenge

## 131 Solution

### 132 Calculating aggregates with agg()

### 133 Same-shape Transforms

### 134 More flexibility with applymap()

### 135 Element-wise operations with applymap()

# 136 Skill challenge

## 137 solution

# **End of file note**

### **End was just a lie**

https://en.wikipedia.org/wiki/Lazy_evaluation

