
import pandas as pd
indVarName = "Food productiom"
indVarName2 = "Renewable water"
indVarNames = [indVarName,indVarName2]
countryName = "Afghanistan"
countryCode = "AFG"
filename= {}
filename[indVarName] = "API_AG.PRD.FOOD.XD_DS2_en_csv_v2_5873190.csv"
filename[indVarName2] = "API_ER.H2O.INTR.PC_DS2_en_csv_v2_5873461.csv"


def load_data(indVarName, countryName):
    dir = "./data/"
    data = pd.read_csv(dir + filename[indVarName],index_col=[0,1,2,3],header=[2])
    data.index = data.index.get_level_values("Country Name")
    #print(data)
    df_country = data.loc[countryName]
    nan_value_count = df_country.isnull().sum()
    year_count = len(df_country.values)
    print("for indicator ", indVarName, " in country ", countryName, " ", year_count- nan_value_count, " values for years found, missing ",nan_value_count, " years")
    return df_country

def get_idx_nan(data):
    return [i for i, x in enumerate(data.isnull()) if x]

def get_idx_nan_indicators(data_indicators):
    return set([idx for data_year in data_indicators for idx in get_idx_nan(data_year)])

data_indicators = []
for indVarName in indVarNames:
    data_indicators.append(load_data(indVarName, countryName))

print(get_idx_nan_indicators(data_indicators))
