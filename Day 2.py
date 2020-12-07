import pandas as pd

i = 0
df = pd.read_excel("Puzzel 2.xlsx")

# Clean Up

df["Policy"] = df["Policy"].str.strip()
df["Password"] = df["Password"].str.strip()

# Convert columns from Object to String
df['Policy'] = df['Policy'].convert_dtypes()
df['Password'] = df['Password'].convert_dtypes()

# Getting Columns with required info to check passwords
df["Letter"] = [x.strip()[-1] for x in df['Policy']]
df["LowerLimit"] = [x.split("-", -1)[0] for x in df['Policy']]
df["UpperLimit"] = [x.split("-", -1)[1].split(" ", -1)[0] for x in df['Policy']]

df["Letter"] = df["Letter"].convert_dtypes()
df["LowerLimit"] = df["LowerLimit"].astype('int')
df["UpperLimit"] = df["UpperLimit"].astype('int')

# Loop through elements and check every row
count = 0
for i in range(0, 1000):
    L = df["Letter"].iloc[i]
    S = df["LowerLimit"].iloc[i]
    SP = df["UpperLimit"].iloc[i]
    P = df["Password"].iloc[i]
    if P[S-1] == L and P[SP-1] == L:
        pass
    elif P[S-1] != L and P[SP-1] != L:
        pass
    else:
        count += 1

    print(count)

