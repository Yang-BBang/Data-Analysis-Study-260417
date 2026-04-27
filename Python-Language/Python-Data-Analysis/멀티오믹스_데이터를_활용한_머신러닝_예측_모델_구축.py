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
# plt.figure(figsize=(12, 10))
# corr = df.corr()
# sns.heatmap(corr, annot=False, cmap='coolwarm')
# plt.title("Multi-Omics Correlation Matrix")
# plt.show()



# 라벨링: 인덱스에 'DIS'가 포함되면 1(질환), 아니면 0(정상)
df['Target'] = [1 if 'DIS' in idx else 0 for idx in df.index]

print(df['Target'].value_counts())

X = df.drop('Target', axis=1)
y = df['Target']

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123, stratify=y
)

# 모델 생성 및 학습
model = RandomForestClassifier(n_estimators=100, random_state=123, n_jobs=-1)
model.fit(X_train, y_train)


#  2) ROC 커브와 AUC
# 모델의 분류 성능을 시각화하여 예측 성능을 평가
# [Code 셀]
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='red', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.show()