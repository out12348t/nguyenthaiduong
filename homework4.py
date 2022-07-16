import pandas as pd
df = pd.read_csv('data/data1.csv')


print(df['GioiTinh'])

print(df['GioiTinh'][8])

# sr1 = pd.Series([ 8.0, 10.0, 6.0, 4.0, 5.0, 333333333333333, 9.0, 8.0, 10.0, 2.0, 3.0, 4.0 , 6.0, 7.0, 8.0, 3.0, 9.0, 10.0, 5.0, 4.0])
# df['DiemTrungBinh'] = sr1
df["DiemToan"] = pd.to_numeric(df["DiemToan"])
df["DiemLy"] = pd.to_numeric(df["DiemLy"])
df["DiemHoa"] = pd.to_numeric(df["DiemHoa"])

df["DiemTrungBinh"] = (df["DiemToan"] + df["DiemLy"] + df["DiemHoa"]) / 3
df.to_csv("data1.csv")
print(df)

df["a"] = (df["DiemLy"] + df["DiemHoa"]) / 2 
print(df.loc[df['GioiTinh'] == 'Nam'])


print(df.loc[df['GioiTinh'] == 'Nữ'])

print(df.loc[df['GioiTinh'] > 8])

print(df.loc[df['a'] > 5])