import pandas as pd
from sklearn.model_selection import train_test_split

# Membaca dataset dari file yang diunggah
df = pd.read_csv("data/housing.csv")

# Memisahkan data menjadi set training dan testing
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Menyimpan dataset train dan test ke file CSV
train_df.to_csv('housing_train.csv', index=False)
test_df.to_csv('housing_test.csv', index=False)

print("Dataset berhasil dibagi dan disimpan!")
print(f"Ukuran dataset train: {train_df.shape[0]} baris")
print(f"Ukuran dataset test: {test_df.shape[0]} baris")
print("File yang dihasilkan: housing_train.csv dan housing_test.csv")