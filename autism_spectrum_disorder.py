# -*- coding: utf-8 -*-
"""Autism spectrum disorder.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nQzqRVqlu9YnHJ81iMgsHtYxtEAtq7-3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

df = pd.read_csv('/content/Autism_Data.csv')
print(df.head())

from google.colab import drive
drive.mount('/content/drive')

df.shape

df.info()

df.describe().T

df['ethnicity'].value_counts()

print(df.columns)

# Check for a typo in the column name
if 'relation' in df.columns:
    print("Column 'relation' exists.")
else:
    print("Column 'relation' does not exist.")

print(df.head())

df = df.replace({'yes':1, 'no':0, '?':'Others', 'others':'Others'})

pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Assuming you've already read the CSV file into the DataFrame
df = pd.read_csv('/content/Autism_Data.csv')

# Now, you can create the pie chart
plt.pie(df['Class/ASD'].value_counts().values, autopct='%1.1f%%')
plt.show()

ints = []
objects = []
floats = []

for col in df.columns:
    if df[col].dtype == int:
        ints.append(col) # Replaced possible tab with 4 spaces
    elif df[col].dtype == object:
        objects.append(col) # Replaced possible tab with 4 spaces
    else:
        floats.append(col) # Replaced possible tab with 4 spaces

print("Original 'ints' list:", ints)

!pip install seaborn
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

# Assuming 'df' is already loaded with your data
ints = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']  # Example columns

plt.subplots(figsize=(15, 15))

for i, col in enumerate(ints):
    plt.subplot(4, 3, i+1)

    # Use the correct seaborn syntax
    sb.countplot(x=col, hue='gender', data=df)

    plt.tight_layout()  # Adjust the layout

plt.show()

import matplotlib.pyplot as plt
import seaborn as sb

# Assuming 'df' is already loaded with your data
# Define the list of columns you want to plot
ints = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10']

# Set the size of the figure
plt.subplots(figsize=(15, 15))

# Loop through the columns in the 'ints' list
for i, col in enumerate(ints):
    plt.subplot(4, 3, i + 1)  # Create a subplot for each column

    # Use Seaborn's countplot with the correct syntax
    sb.countplot(x=col, hue='Class/ASD', data=df)

    # Adjust layout to prevent overlap
    plt.tight_layout()

# Display the plots
plt.show()

plt.subplots(figsize=(15, 15))

for i, col in enumerate(ints):
    plt.subplot(4, 3, i + 1)
    sns.countplot(data=df, x=col, hue='Class/ASD')

plt.tight_layout()
plt.show()

plt.subplots(figsize=(15, 15))

for i, col in enumerate(objects):
    plt.subplot(5, 3, i + 1)
    sns.countplot(data=df, x=col, hue='Class/ASD')
    plt.xticks(rotation=60)

plt.tight_layout()
plt.show()

df = pd.read_csv('/content/Autism_Data.csv')

print(df.columns)

import pandas as pd

# Load the dataset
file_path = '/content/Autism_Data.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe to understand its structure
df.head(), df.columns

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Assuming floats is a list of column names
n_cols = len(floats)
n_rows = int(np.ceil(n_cols / 2))  # Adjusting rows to fit all columns in pairs

plt.figure(figsize=(15, 5 * n_rows))  # Adjusting figure size to accommodate rows

for i, col in enumerate(floats):
    plt.subplot(n_rows, 2, i + 1)  # Creating subplots in a grid of (n_rows, 2)
    sns.histplot(df[col], kde=True)  # Adding kde=True to show the kernel density estimate
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

num_cols = len(floats)
num_rows = 1  # You can adjust the number of rows as needed

plt.figure(figsize=(15, 5))
for i, col in enumerate(floats):
    plt.subplot(num_rows, num_cols, i + 1)
    sns.boxplot(data=df, x=col)

plt.tight_layout()
plt.show()

df = df[df['result']>-5]
df.shape

def convertAge(age):
    try:
        age = float(age)  # Convert 'age' to a float (assuming it's a string or non-numeric)
        if age < 4:
            return 'Toddler'
        elif age < 12:
            return 'Child'
        elif age < 20:
            return 'Teenager'
        else:
            return 'Senior'
    except (ValueError, TypeError):
        return 'Invalid'  # Handle non-numeric or invalid values

df['ageGroup'] = df['age'].apply(convertAge)

plt.figure(figsize=(10, 5))
sns.countplot(x=df['ageGroup'], hue=df['Class/ASD'])
plt.show()

print(df.head())

plt.figure(figsize=(10, 5))
sns.countplot(x=df['sum_score'], hue=df['Class/ASD'])
plt.show()

df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Apply the log transformation, adding 1 to avoid issues with zero or negative values
df['age'] = df['age'].apply(lambda x: np.log(x + 1))

plt.figure(figsize=(10, 5))
sns.distplot(df['age'])
plt.show()

from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

def encode_labels(data):
    for col in data.columns:
        if data[col].dtype == 'object':
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col])
    return data

# Apply label encoding
df = encode_labels(df)

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), annot=True, cbar=False, cmap="coolwarm")
plt.show()

import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'ID': [1, 2, 3],
    'age_desc': ['adult', 'child', 'adult'],
    'used_app_before': [1, 0, 1],
    'austim': [0, 1, 0],
    'feature1': [10, 20, 30],
    'feature2': [0.1, 0.2, 0.3],
    'Class/ASD': [1, 0, 1]
})

# Columns to remove
removal = ['ID', 'age_desc', 'used_app_before', 'austim']

# Prepare features and target
features = df.drop(removal + ['Class/ASD'], axis=1)
target = df['Class/ASD']

print("Features:\n", features)
print("Target:\n", target)

print(df.columns)

removal = ['age_desc', 'Class/ASD']
features = df.drop(removal, axis=1)
target = df['Class/ASD']

X_train, X_val, Y_train, Y_val = train_test_split(features, target, test_size = 0.2, random_state=10)

# As the data was highly imbalanced we will balance it by adding repetitive rows of minority class.
ros = RandomOverSampler(sampling_strategy='minority',random_state=0)
X, Y = ros.fit_resample(X_train,Y_train)
X.shape, Y.shape

# Normalizing the features for stable and fast training.
scaler = StandardScaler()
X = scaler.fit_transform(X)
X_val = scaler.transform(X_val)

for i in range(5):
    pass  # Empty block, does nothing

for i in range(5):
    print(i)  # Indented code block