import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("gurgaon_real_estate.csv")

# 1. DATA CLEANING

# Standardize column name
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_' )

# Remove duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates()

print("Duplicate rows removed:", duplicates_before)


# 2. NUMERICAL COLUMNS CLEANING

df['price'] = df["price"].astype(str).str.replace(",", "", regex=False).astype(float)
df['area'] = df["area"].astype(str).str.replace(",", "", regex=False).astype(int)
df['rate_per_sqft'] = df["rate_per_sqft"].astype(str).str.replace(",", "", regex=False).astype(int)


# 3. CATEGORICAL COLUMNS CLEANING

df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()


# 4. DATA QUALITY CHECK

print("\n========== DATA QUALITY REPORT ==========")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows after cleaning:", df.duplicated().sum())
print("\nInvalid price values:", (df['price'] <= 0).sum())
print("Invalid area values:", (df['area'] <= 0).sum())
print("Invalid rate per sqft values:", (df['rate_per_sqft'] <= 0).sum())


# 5. BASIC STATISTICS

print("Average price:", df['price'].mean())
print("Median price:", df['price'].median())
print("Minimum price:", df['price'].min())
print("Maximum price:", df['price'].max())

print("Average area:", df['area'].mean())
print("Average rate per sqft:", df['rate_per_sqft'].mean())


# 6. PRICE DISTRIBUTION

plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=50, kde=True)
plt.title('Distribution of Property Prices')
plt.xlabel('Price')
plt.ylabel('Number of Properties')
plt.show()


# 7. AREA VS PRICE

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='area', y='price')
plt.title('Property Area vs Price')
plt.xlabel('Area (sq.ft)')
plt.ylabel('Price')
plt.show()


# 8. LOCALITIES BY AVERAGE PRICE

top_localities = (
    df.groupby('locality')['price'].mean().sort_values(ascending=False).head(10)
)
plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_localities.values,
    y=top_localities.index
)

plt.title('Top 10 Localities by Average Property Price')
plt.xlabel('Average Price')
plt.ylabel('Locality')

plt.show()


# 9. BHK ANALYSIS

print("\nBHK Distribution:")
print(df['bhk_count'].value_counts().sort_index())

sns.countplot(data=df, x='bhk_count')
plt.title('Properties by BHK')
plt.show() 


# 10. AVERAGE PRICE BY BHK

print(df.groupby('bhk_count')['price'].mean().round(2))

sns.barplot(data=df, x='bhk_count', y='price')
plt.title('Average Price by BHK')
plt.show()


# 11. PROPERTY TYPE

print(df['flat_type'].value_counts())

sns.countplot(data=df, y='flat_type')
plt.title('Properties by Type')
plt.show()


# 12. AVERAGE PRICE BY PROPERTY TYPE

print(df.groupby('flat_type')['price'].mean().round(2))

sns.barplot(data=df, y='flat_type', x='price')
plt.title('Average Price by Property Type')
plt.show()
      

# 13. TOP 10 LOCALITIES BY Price/sq.ft

top_localities = df.groupby('locality')['rate_per_sqft'].mean().nlargest(10)

print(top_localities.round(2))
top_localities.plot(kind='barh', figsize=(8,5))
plt.title('Top 10 Localities by Rate/sq.ft')
plt.xlabel('Average Rate/sq.ft')
plt.show()


# 14. PRICE OUTLIERS

Q1, Q3 = df['price'].quantile([.25, .75])
IQR = Q3 - Q1
outliers = df[df['price'] > Q3 + 1.5 * IQR]

print("Price outliers:", len(outliers))
print(f"Outlier %: {len(outliers)/len(df)*100:.2f}%")


