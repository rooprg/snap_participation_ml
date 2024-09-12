import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the full path to the data directory
data_dir = '/Users/mauriciogil/Desktop/snap_participation_ml/data/'

# Load the datasets from the 'data' subfolder, specifying that the first row contains column headers
household_df = pd.read_csv(data_dir + 'faps_household_puf.csv', header=0)
access_df = pd.read_csv(data_dir + 'faps_access_puf.csv', header=0)
fahevent_df = pd.read_csv(data_dir + 'faps_fahevent_puf.csv', header=0)
fafhevent_df = pd.read_csv(data_dir + 'faps_fafhevent_puf.csv', header=0)

# Inspect the data
print(household_df.head())
print(access_df.head())
print(fahevent_df.head())
print(fafhevent_df.head())

# Check for missing values
print(household_df.isnull().sum())
print(access_df.isnull().sum())
print(fahevent_df.isnull().sum())
print(fafhevent_df.isnull().sum())

# Select relevant columns from household_df
# Assuming the column names correspond to the provided titles
X_household = household_df[['monthly_income', 'income_excluding_input', 'housing_costs', 'medical_expenses', 'household_size']]  # Adjust column names
X_access = access_df[['distance_to_snap_store']]  # Adjust if needed

# Merge datasets
# Common key 'household id hhnum'
# Adjust the key if needed
X = pd.merge(X_household, X_access, how='inner', on='hhnum')  # Adjust key if needed

# Check the first few rows of the merged dataset
print(X.head())

# Rename columns
X.columns = ['monthly_income', 'income_excluding_input', 'housing_costs', 'medical_expenses', 'household_size', 'distance_to_snap_store']

# Check for missing values in the merged dataset
print(X.isnull().sum())

# Handle missing values
X = X.fillna(X.mean())  # Fill missing values with the mean (adjust strategy if needed)

# Inspect the cleaned dataset
print(X.describe())

# Plot histograms for continuous variables
X[['monthly_income', 'income_excluding_input', 'housing_costs', 'medical_expenses']].hist(bins=30, figsize=(12, 8))
plt.suptitle('Distribution of Continuous Features')
plt.show()

# Calculate correlation matrix
correlation_matrix = X.corr()

# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Boxplot for household income vs. SNAP participation

sns.boxplot(x='SNAP_participation', y='monthly_income', data=X)
plt.title('Household Income vs SNAP Participation')
plt.show()

# Pair plot 
sns.pairplot(X)  
plt.show()

