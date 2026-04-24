# DATA-ANALYSIS-STUDY

R과 Python을 활용한 데이터 분석 학습 및 프로젝트 기록 저장소입니다. 현재 생물정보학 데이터와 질환 예측 모델링을 중심으로 분석 역량을 쌓아가고 있습니다.

---

## Repository Structure

### [Python-Language](./Python-Language)
* **Python-Basic**: 기초 문법 및 데이터 구조 학습
* **Python-Data-Analysis**: 라이브러리를 활용한 데이터 처리 실습

### [R-Language](./R-Language)
* **R-Basic**: R 프로그래밍 기초 및 통계 기초
* **R-Data-Analysis**: 실전 데이터 분석 스크립트
  * **당뇨병 유무 예측 및 핵심 인자 발굴**: 분류 모델 구축 및 변수 분석
  * **대사체 데이터를 활용한 질환 핵심 마커 발굴**: 바이오마커 추출 및 시각화

---

## Core Skills (Current)

### Languages
* `R`: 데이터 분석 및 시각화 주력 사용
* `Python`: 기초 문법 및 데이터 분석 환경 활용

### Analysis & Visualization
* **Metabolomics**: 대사체 데이터를 활용한 기초 분석
* **Visualizations**: `ggplot2`를 활용한 데이터 시각화 (PCA, Volcano Plots 등)
* **Modeling**: 질환 유무 예측을 위한 기초 모델링 및 ROC Curve 분석

---

## Tools
* `VS Code`, `RStudio`, `Git`, `GitHub`

---

## Featured Projects

### 1️⃣ 당뇨병 유무 예측 및 임상 핵심 인자 발굴 ([리포트 보기](https://htmlpreview.github.io/?https://github.com/Yang-BBang/Data-Analysis-Study-260417/blob/main/R-Language/R-Data-Analysis/당뇨병_유무_예측_및_핵심_인자_발굴.html))
임상 데이터를 활용하여 질환 예측에 기여하는 핵심 변수를 선별하고 통계적으로 검증한 프로젝트입니다.
* **Key Insight:** 
    * `Glucose`가 당뇨병 예측의 압도적 주요 인자임을 확인 하였으며, `Mass`, `pedigree`, `Age` 또한 주요 인자임을 확인 ($P < 0.05$).
    * **비판적 전처리:** `Pregnant` 변수의 이상치를 제거한 후 재분석을 수행하여, 측정 오류가 통계적 유의성을 왜곡할 수 있음을 증명 ($P$-value $0.006 \rightarrow 0.79$).

### 2️⃣ 대사체 데이터를 활용한 질환 핵심 마커 발굴 ([리포트 보기](https://htmlpreview.github.io/?https://github.com/Yang-BBang/Data-Analysis-Study-260417/blob/main/R-Language/R-Data-Analysis/대사체_데이터를_활용한_질환_핵심_마커_발굴.html))
가상의 대사체 데이터 중 질환군과 대조군을 구분 짓고 유의미한 마커를 발굴하는 프로세스를 연습했습니다.
* **Key Insight:** 
    * **Volcano Plot**을 활용하여 Fold Change와 P-value를 동시에 만족하는 유의 대사체 선별.
    * **PCA & Heatmap** 시각화를 통해 그룹 간의 명확한 패턴 차이 및 변별력 증명.

---

## Analysis Visualizations
분석 과정에서 도출된 핵심 시각화 결과물입니다.

| PCA Plot | ROC Curve |
| :---: | :---: |
| ![PCA](./Graph/PCA_Plot.png) | ![ROC](./Graph/ROC_Curve.png) |
| **Volcano Plot** | **Heatmap** |
| ![Volcano](./Graph/Volcano_Plot.png) | ![Heatmap](./Graph/Heatmap.png) |

---

## Next Step & Future Goals
* **Python Integration:** R에서 선별된 핵심 인자들을 기반으로 Python `Scikit-learn`을 활용한 머신러닝 예측 모델(Random Forest 등) 고도화 예정.
* **Multi-omics Integration:** 전사체(Transcriptomics)와 대사체(Metabolomics) 데이터를 통합하여 생물학적 기전을 심층 분석하는 연구 지향.
