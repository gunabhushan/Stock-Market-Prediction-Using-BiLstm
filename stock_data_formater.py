import pandas as pd

dfmacd = pd.read_csv("ibmmacd.csv")
df = pd.read_csv("ibm.csv")
dfmfi = pd.read_csv("ibmmfi.csv")
startdate = dfmfi['time'][0]
enddate = "2000-01-01"
# print(startdate)

df = df.loc[(df["timestamp"] >= enddate ) & (df["timestamp"] <= startdate)]
dfmacd = dfmacd.loc[(dfmacd["time"] >= enddate ) & (dfmacd["time"] <= startdate)]
dfmfi = dfmfi.loc[(dfmfi["time"] >= enddate ) & (dfmfi["time"] <= startdate)]
res = df['adjusted_close']
dffinal = pd.concat([df[['open','high','low','volume']], dfmacd['MACD'], dfmfi["MFI"]],axis=1)

df_min_max_scaled = dffinal.copy()

for column in df_min_max_scaled.columns:
    df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())    
  

print(df_min_max_scaled)