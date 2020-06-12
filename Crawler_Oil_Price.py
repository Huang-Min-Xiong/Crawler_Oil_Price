import json
import pandas as pd
from datetime import datetime

#取得油價資訊
def get_oil_price():
    Oil_url='https://www2.moeaboe.gov.tw/oil102/oil2017/A01/A0108/tablesprices.asp'
    Data = pd.read_html(Oil_url)[0]  #取得網頁上的表格資訊
    #print(Data) #顯示所有資訊
    #Today='2020/06/8' #目前日期(測試用)
    Today = datetime.now().strftime("%Y/%m/%d") #目前日期
    Date_Of_Implementation=Data.loc[1][6][0:10] #取得最新日期
    #print(Date_Of_Implementation) #顯示最新日期

    if Today == str(Date_Of_Implementation):  # 判斷今天日期是否與最新日期相同，不相同則回傳False
        Data.loc[0:2].to_json(r'./Oil_Price.json') #將前三列的數據存到json檔
        Oil_Supplier=pd.read_json(r'./Oil_Price.json')[0] #Json內容(油品供應商)
        Unleaded_Gas_98=pd.read_json(r'./Oil_Price.json')[1] #Json內容(98無鉛汽油)
        Unleaded_Gas_95=pd.read_json(r'./Oil_Price.json')[2] #Json內容(95無鉛汽油)
        Unleaded_Gas_92=pd.read_json(r'./Oil_Price.json')[3] #Json內容(92無鉛汽油)
        Diesel=pd.read_json(r'./Oil_Price.json')[4] #Json內容(超(高)級柴油)
        Sales_Unit=pd.read_json(r'./Oil_Price.json')[5] #Json內容(計價單位)
        Date=pd.read_json(r'./Oil_Price.json')[6] #Json內容(施行日期)
        Date[1]=str(Date[1][:11])
        Date[2]=str(Date[2][:11])
        print('         日期      油品供應商  98汽油 95汽油 92汽油 計價單位')    
        print(Date[1:]+'   '+Oil_Supplier[1:]+'   '+Unleaded_Gas_98[1:]+'  '+Unleaded_Gas_95[1:]+'  '+Unleaded_Gas_92[1:]+'  '+Sales_Unit[1:])
        #return True
    else:
        print("\n{} →→ 油價尚未調整".format(Today))
        #return False


if __name__ == "__main__":
    get_oil_price() #調用get_oil_price()函數
    
