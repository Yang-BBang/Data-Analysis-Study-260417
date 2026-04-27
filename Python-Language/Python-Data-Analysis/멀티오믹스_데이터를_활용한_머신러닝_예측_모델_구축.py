# [Code 셀]
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, roc_curve, auc

# 데이터 로드
df = pd.read_csv('/Users/seunghoyang/Desktop/Data-Analysis-Study:/Python-Language/Python-Data-Analysis/MultiOmics_Final_Dataset.csv', index_col=0)
print(f"데이터 구조: {df.shape}")





# [Code 셀]
plt.figure(figsize=(12, 10))
corr = df.corr()
sns.heatmap(corr, annot=False, cmap='coolwarm')
plt.title("Multi-Omics Correlation Matrix")
plt.show()