import pandas as pd 
import csv
df=pd.read_csv("totalstars2.csv")
df
df.columns
df.drop
df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity'],axis=1,inplace=True)
df
finaldata=df.dropna()
finaldata
finaldata.reset_index(drop=True,inplace=True)
finaldata
finaldata.to_csv("datacleaned.csv")
finaldata.info()
finaldata.describe()
finaldata.head(5)
finaldata.dtypes