import pandas as pd

test_a = pd.read_csv('test_a.csv',encoding='gbk')

print(test_a['puzzle'][0])