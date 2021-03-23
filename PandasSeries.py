import pandas as pd
data_ls = [10,20,'kong',15.05,'มะละกอ'] #// list
data_tp = (10,20,'kong',15.05,'มะละกอ') #// tuple
ps = pd.Series(data_ls)
ps = pd.Series(data_tp)
print(ps)

#### // Define Series by self index //
import pandas as pd
import numpy as np
items = ['องุ่น','กล้วย','มะละกอ']
idx =[50,20,30]
ps = pd.Series(items,index=idx)
ps

############ // สร้าง Series จาก Dictionary ############
import pandas as pd
data = {'องุ่น':50,'กล้วย':20,'มะละกอ':30}  #// Dictionary
ps = pd.Series(data)
ps
