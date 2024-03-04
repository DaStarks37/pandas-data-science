import os
import pandas as pd
terminalsize = os.get_terminal_size()
dividerline = "_" * terminalsize.columns

df = pd.read_csv("telco_churn.csv")
df.dropna(inplace=True)
temporarydict = {"col1": [1, 2, 3], "col2": [4, 5, 6], "col3": [7, 8, 9]}
dfdict = pd.DataFrame.from_dict(temporarydict)
state = df.copy()
state.set_index("State", inplace=True)
df["SuperColumn"] = df["Total night minutes"] + df["Total intl minutes"]
def updateinlist(columntoupdate, value):
    df[columntoupdate] = value
pastfirst = 0

printlist = [df.head(10), df.tail(10), df.columns, df.dtypes, df.describe, df.State, df["International plan"],df.State.unique(), df[df["International plan"]== "No"], df[(df["International plan"]== "No") & (df["Churn"]==False)], df.iloc[0:16], df.iloc[14,0], state.loc["OH"], df.drop("Area code", axis=1), df.isnull().sum(), updateinlist("SuperColumn", 100), df.head(16)]


def printall():
    for item in printlist:     
        print(item)
        print(dividerline)




printall()
input("\nPress ENTER to exit. ")