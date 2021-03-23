การสร้าง DataFrame

สามารถ สร้างได้จากหลายวิธี
1. Tuple และ list
2. Series
3. numpy
4. CSV

การสร้าง DataFrame จาก List และ tuple
import pandas as pd
from pandas.io import excel
data_ls = [10,20,'kong',15.05,'มะละกอ'] #// list
data_tp = (10,20,'kong',15.05,'มะละกอ') #// tuple
df = pd.DataFrame(data_ls)
df = pd.DataFrame(data_tp)
df

การสร้าง DataFrame แบบกำหนด คอลัมน์
import pandas as pd
data =[15,20,23,30]
cols =['Age']
df = pd.DataFrame(data,columns=cols)
df

การสร้าง DataFrame จาก List แบบหลายมิติ
import pandas as pd
data =[
        ['คีบอร์ด','อุปกรณ์คอม',1200],
        ['ตุ๊กตา','ของเล่น',900],
        ['iphone 12','มือถือ',30000]
    ]

cols=['Name','Category','Price']
df =pd.DataFrame(data,columns=cols)
df


การสร้าง DataFrame จาก List หลายตัวด้วย zip
import pandas as pd
item1 = ['คีย์บอร์ด','อุปกรณ์คอม',1200]
item2 = ['ตุ๊กตา','ของเล่น',900]
item3 = ['iphone 12','มือถือ',30000]

data = list(zip(item1,item2,item3))
cols=['Name','Category','Price']
df =pd.DataFrame(data,columns=cols)
df

### ผลลัพธ์จะออกมาไม่ถูกต้อง ถ้า้ใช้ zip มันจะกลับทิศ

import pandas as pd
ProductName = ['คีย์บอร์ด','ตุ๊กตา','มือถือ']
Category = ['อุปกรณ์คอม','ของเล่น','iphone 12']
Price = [1200,900,30000]

data = list(zip(ProductName,Category,Price))
cols=['Name','Category','Price']
df =pd.DataFrame(data,columns=cols)
df



การสร้าง DataFrame จาก Dictionary
import pandas as pd
data =[
{"Name":"คีย์บอร์ด","Category":"อุปกรณ์คอม","Price":1200},
{"Name":"ตุ๊กตา","Category":"ของเล่น","Price":900},
{"Name":"Iphone 12","Category":"มือถือ","Price":30000}
]

df=pd.DataFrame(data)
df

df.set_index(["Name"])
df.set_index(["Name"],inplace=True)


การสร้าง DataFrame จาก Series
import pandas as pd
name = ['คีย์บอร์ด','ตุ๊กตา','iphone 12']
Category = ['อุปกรณ์คอม','ของเล่น','มือถือ']
price = [1200,900,30000]
names =pd.Series(name)
categorys=pd.Series(Category)
prices=pd.Series(Price)

frame ={'Name':names,'Category':categorys,'Price':prices}

df=pd.DataFrame(frame)


การ export Dataframe ไป csv

DataFrame.to_csv(ตำแหน่งไฟล์,attribute)

Attribute
  header ต้องการบันทึกส่วนหัวคอลัมน์หรือไม่ (True/False) (Default:True)
  index ต้องการบันทึกเลข Index หรือไม่ (True/False) (Default: True)


df.to_csv ("products.csv",)
df.to_csv ("products2.csv",index=False)


DataFrame อ่านเอกสาร CSV
import pandas as pd
df = pd.read_csv('products.csv',encoding='utf-8')
df.head()
#usersDf =  pd.read_csv('users.csv', sep='__'  , engine='python')


import pandas as pd
cols = ['Name','Price']
df = pd.read_csv('products.csv',encoding='utf-8',usecols=cols)

df = pd.read_csv('products.csv',encoding='utf-8',usecols=cols,index_col="Name")


อ่านเอกสาร excel
import pandas as pd
df = pd.read_excel("dataupdate.xlsx","weather",encoding="utf-8",index_col="Day")
df

df = pd.read_excel("dataupdate.xlsx","score",encoding="utf-8",index_col="Day")



df[df.Event.str.match("ฝนตก")]

df.loc[(df.Event=="ฝนตก") & (df.Temperature>=35)]


df.loc[(df.Temperature==18) | (df.Temperature==20) | (df.Temperature==25) | (df.Temperature==35)]
df.loc[(df.Temperature.isin([18,20,25,35]))]

df.loc[(df.Temperature.isin([30,35]))][df.Event=="แดดร้อน"]
