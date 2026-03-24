import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

df = pd.read_csv("~/Downloads/diabetes.csv")
print(df.head())
print(df.columns)

df_filtered = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'Age']]

print(df_filtered.columns)

matriu = df_filtered.corr(method='pearson')
print(matriu)

df_matriu = pd.DataFrame(matriu)
df_matriu.to_csv('matriu.csv', index=False)

plt.figure(figsize=(8,6))
sns.heatmap(matriu, xticklabels=df_matriu.columns, yticklabels=df_matriu.columns, cmap='coolwarm', annot=True, center=0)

plt.title("Matriu de correlació de variables relacionades amb la Diabetis")
plt.savefig("correlation_matrix.png", dpi=300, bbox_inches='tight')
plt.show()