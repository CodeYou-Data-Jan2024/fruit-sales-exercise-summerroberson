import pandas as pd

df_fruit = pd.DataFrame (columns = ["Apples" , "Bananas" ])

df_fruit

new_data = {
    "Apples" : [35 , 41],
    "Bananas" : [41 , 34]
}

df_sales = pd.DataFrame(new_data, index=["2017 Sales","2018 Sales"])

df_sales
