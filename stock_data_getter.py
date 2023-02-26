import requests
# apiKey = 'SD6YKXN125Z0COGS'
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo&datatype=csv'

url = 'https://www.alphavantage.co/query'

apiParams = {
    'function' : 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol' : 'IBM',
    'outputsize' : 'full',
    'datatype' : 'csv',
    'apikey' : 'SD6YKXN125Z0COGS'
}
macdApiParams = {
    'function' : 'MACD',
    'symbol' : 'IBM',
    'interval' : 'daily',
    'series_type' : 'open',
    'outputsize' : 'full',
    'datatype' : 'csv',
    'apikey' : 'SD6YKXN125Z0COGS'
}
mfiApiParams = {
    'function' : 'MFI',
    'symbol' : 'IBM',
    'interval' : 'daily',
    'time_period' : '14',
    'outputsize' : 'full',
    'datatype' : 'csv',
    'apikey' : 'SD6YKXN125Z0COGS'
}

req = requests.get(url,apiParams)
data = req.content
datafile = open("ibm.csv",'wb')
datafile.write(data)
datafile.close()

req = requests.get(url,mfiApiParams)
data = req.content
mfifile = open('ibmmfi.csv','wb')
mfifile.write(data)
mfifile.close()

req = requests.get(url,macdApiParams)
data = req.content
macdfile = open('ibmmacd.csv','wb')
macdfile.write(data)
macdfile.close()