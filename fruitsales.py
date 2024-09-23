import pandas as pd

data = {
    "Apples" : [35 , 41],
    "Bananas" : [41 , 34]
}

df_sales = pd.DataFrame(data, index=["2017 Sales","2018 Sales"])

print (df_sales)
