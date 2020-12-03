import pandas as pd

## getting the input from excel into a dataframe
df = pd.read_excel("Puzzel 1.xlsx")

for n in df["Numbers"]:
    for a in df["Numbers"]:
        for x in df["Numbers"]:
            if n+a+x == 2020:
                print(n*a*x)



