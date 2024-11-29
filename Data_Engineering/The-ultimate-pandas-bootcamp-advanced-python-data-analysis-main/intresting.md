```python
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

String parse time:

`datetime.strptime()`


[Formating](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) <-- The following is a list of all the format codes that the 1989 C standard requires, and these work on all platforms with a standard C implementation.

```python
from dateutil import parser
parser.parse('22 april 2068 at 4pm and 17 minutes 20 seconds')
```

[TimeStamp](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html) <-- doc

```python
pd.Timestamp('4/7/1776')
pd.to_datetime('4/7/1776',dayfirst=True)
```

```python
pd.read_csv(oil_url, index_col=0, parse_dates=True)
```

# Links:

[keyboard-shortcuts-macos.pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

[Next line in markdown line](https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops#markdown-files-or-widgets)

----

```
two spaces and then enter.
```

> Single line quote
>> Nested quote
>> multiple line
>> quote
>>> Third quote??  
>>>> Forth quote???  
>>> 3th second time?  
> Single line quote

> 2th second time?   
>> and the last time the first line.  

```python
!pip show seaborn
```

```python
!pip install seaborn
Use '%pip install' instead of '!pip install'Jupyter

```

```bash
python3 -m notebook
```

```python
from IPython.display import display, HTML

display(HTML(hobbies.to_html()))
```