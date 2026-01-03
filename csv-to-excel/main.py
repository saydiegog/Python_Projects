import pandas as pd
import openpyxl

def read_csv(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df
    except:
        print("Error reading CSV file!")

def cleaning(df):
    new_df = df.fillna("-")
    new_df = new_df.drop_duplicates()
    return new_df

def conversion(clean_df):
    clean_df.to_excel("output.xlsx", index=False)
    print("Conversion succesfull!")

csv = input("enter csv file path: ")
df = read_csv(csv)

if df is None:
    print("Bye!")
else:
    new_df = cleaning(df)
    conversion(new_df)


