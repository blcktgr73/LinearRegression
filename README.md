# 🏠 Linear Regression 모델 최적화 프로젝트

## 📋 프로젝트 개요
California Housing Dataset을 사용한 주택 가격 예측 모델 최적화 학습 프로젝트입니다.
체계적인 머신러닝 파이프라인을 통해 데이터 분석부터 모델 최적화까지 전 과정을 다룹니다.

## 🎯 학습 목표
- ✅ 정규화(StandardScaler) 적용 효과 이해
- ✅ L1/L2 정규화(Ridge, Lasso) 비교 분석
- ✅ GridSearchCV를 통한 하이퍼파라미터 최적화
- ✅ 종합적인 모델 성능 분석 및 시각화

## 📁 프로젝트 구조
```
LinearRegression/
├── data/                       # 데이터 파일들
│   └── california_housing_processed.csv  # 처리된 데이터셋
├── notebooks/                  # Jupyter notebooks
│   ├── 01_eda.ipynb           # 탐색적 데이터 분석 (한글 버전)
│   ├── 01_eda_fixed.ipynb     # 탐색적 데이터 분석 (영어/한글 호환)
│   ├── 02_normalization.ipynb # 정규화 비교 분석
│   ├── 03_models.ipynb        # Ridge, Lasso 모델 구현 및 비교
│   ├── 04_optimization.ipynb  # GridSearchCV 하이퍼파라미터 최적화
│   └── 05_analysis.ipynb      # 최종 결과 분석 및 시각화
├── src/                       # Python 모듈
│   └── font_setup.py          # 한글 폰트 설정 유틸리티
├── results/                   # 결과 이미지, 표
├── test_notebook.py           # 노트북 상세 테스트 스크립트
├── quick_test.py              # 노트북 빠른 테스트 스크립트
├── requirements.txt           # 필요 라이브러리 목록
├── .gitignore                 # Git 제외 파일 목록
└── README.md
```

## 🚀 시작하기

### 1. 환경 설정
```bash
pip install -r requirements.txt
```

### 2. Jupyter 실행
```bash
jupyter notebook
```

### 3. 노트북 테스트
```bash
# 빠른 테스트 (오류 확인)
jupyter nbconvert --to notebook --execute --stdout notebooks/01_eda_fixed.ipynb > /dev/null

# 파이썬 스크립트로 테스트
python quick_test.py
```

## 📊 학습 단계

### ✅ 완료된 단계
- [x] **프로젝트 초기 설정** (2025-01-13)
  - Git 저장소 초기화
  - 프로젝트 디렉토리 구조 생성
  - 필요 라이브러리 설치 및 requirements.txt 작성
  - GitHub 연동 및 main 브랜치 생성

- [x] **1단계: 데이터 탐색 (EDA)** (2025-01-13)
  - California Housing Dataset 로드 및 분석
  - 기본 통계량 및 데이터 타입 확인 (20,640개 샘플, 8개 특성)
  - 특성 간 상관관계 매트릭스 생성
  - 지리적 분포 시각화 (위도/경도 활용)
  - 이상치 탐지 및 데이터 분포 분석
  - 한글 폰트 문제 해결 (font_setup.py 모듈 개발)

- [x] **2단계: 정규화 효과 비교** (2025-01-14)
  - StandardScaler 적용 전/후 성능 비교 (성능 차이 거의 없음 확인)
  - 정규화가 각 특성에 미치는 영향 분석 (평균=0, 표준편차=1로 조정)
  - Linear Regression에서 정규화의 한계 이해
  - 정규화의 필요성: Ridge/Lasso, 경사하강법, 신경망에서 중요

- [x] **3단계: 모델 구현 및 비교** (2025-01-14)
  - Linear Regression 기본 모델 구현
  - Ridge Regression (L2 정규화) 구현 및 최적 α 탐색
  - Lasso Regression (L1 정규화) 구현 및 특성 선택 효과 확인
  - 모델별 성능 지표 비교 및 과적합 방지 효과 분석
  - 정규화 경로(Regularization Path) 시각화

- [x] **4단계: 하이퍼파라미터 최적화** (2025-01-14)
  - GridSearchCV를 통한 Ridge/Lasso 최적 α 탐색
  - RandomizedSearchCV와 GridSearchCV 성능/속도 비교
  - 5-fold 교차검증을 통한 정확한 성능 평가
  - 학습 곡선과 검증 곡선을 통한 모델 안정성 분석
  - 파이프라인을 활용한 전처리와 모델링 통합

- [x] **5단계: 결과 분석 및 시각화** (2025-01-14)
  - 최종 모델 성능 비교 (Linear, Ridge, Lasso)
  - Feature Importance 및 Permutation Importance 분석
  - 예측 vs 실제 값 시각화 및 잔차 분석
  - 지리적 예측 분석 및 오차 시각화
  - 프로젝트 전체 결과 요약 및 개선 방향 제시

## 🏆 최종 결과 요약

### 📊 모델 성능 비교
| 모델 | 테스트 R² | 테스트 RMSE | 테스트 MAE |
|------|-----------|-------------|------------|
| **Linear Regression** | 0.6115 | 0.7341 | 0.5225 |
| **Ridge (α=0.001)** | 0.6115 | 0.7341 | 0.5225 |
| **Lasso (α=0.0005)** | 0.6115 | 0.7341 | 0.5225 |

### 🎯 핵심 발견사항
1. **모델 성능**: 모든 모델이 **R² ≈ 0.61**의 유사한 성능 달성
2. **중요 특성**: **MedInc(중위소득)**이 압도적으로 중요한 예측 변수
3. **정규화 효과**: California Housing 데이터는 선형성이 강해 정규화 효과 제한적
4. **지리적 특성**: 해안가 지역에서 예측 오차가 상대적으로 큰 경향
5. **모델 안정성**: 잔차 분석 결과 모델이 전반적으로 안정적

### 📈 특성 중요도 순위 (Permutation Importance)
1. **MedInc** (중위 소득): 0.5279
2. **Latitude** (위도): 0.0388
3. **Longitude** (경도): 0.0378
4. **AveOccup** (평균 거주 인원): 0.0266
5. **HouseAge** (주택 연식): 0.0198
6. **AveRooms** (평균 방 개수): 0.0174
7. **Population** (인구수): 0.0063
8. **AveBedrms** (평균 침실 수): 0.0052

### 📊 데이터셋 특성
- **데이터 크기**: 20,640개 샘플, 8개 특성
- **결측값**: 없음
- **주택 가격 범위**: $15K ~ $500K (평균: $207K)
- **지리적 분포**: 캘리포니아 전역, 해안가 지역이 상대적으로 고가

## 🛠️ 기술 스택
- **데이터 분석**: pandas, numpy
- **머신러닝**: scikit-learn
- **시각화**: matplotlib, seaborn, plotly
- **환경**: Python 3.13, Jupyter Notebook
- **버전 관리**: Git, GitHub

## 💡 개선 방향 및 향후 과제

### 🚀 성능 개선 방안
1. **비선형 모델**: Random Forest, XGBoost 등 트리 기반 모델 시도
2. **특성 엔지니어링**: 지리적 특성 조합, 파생 변수 생성
3. **이상치 처리**: 극값 제거 및 데이터 전처리 개선
4. **앙상블 기법**: 여러 모델 조합으로 성능 향상
5. **딥러닝**: Neural Network를 활용한 비선형 관계 모델링

### 🎓 학습된 핵심 개념
- **정규화의 역할**: 복잡한 모델에서는 필수, 단순 선형 모델에서는 제한적
- **하이퍼파라미터 최적화**: GridSearchCV vs RandomizedSearchCV 장단점
- **모델 평가**: 단순한 성능 지표를 넘어선 종합적 분석의 중요성
- **도메인 지식**: 데이터 이해가 모델 성능 향상의 핵심

### 📝 기술적 학습 노트
- 한글 폰트 문제 해결을 위한 `font_setup.py` 모듈 개발
- matplotlib의 한글 표시 문제는 Windows 환경에서 흔히 발생
- Plotly를 활용한 인터랙티브 지리적 데이터 시각화
- Permutation Importance를 통한 정확한 특성 중요도 측정

## 📊 프로젝트 성과

### ✅ 달성된 목표
- [x] 체계적인 머신러닝 파이프라인 구축
- [x] 정규화 기법들의 효과 비교 분석
- [x] 하이퍼파라미터 최적화 기법 습득
- [x] 종합적인 모델 성능 평가 및 해석
- [x] 실전 데이터 분석 경험 축적

### 🏷️ 버전 히스토리
- **v0.1.0**: 프로젝트 초기 설정 및 EDA
- **v0.2.0**: 정규화 효과 비교 분석
- **v0.3.0**: Ridge, Lasso 모델 구현
- **v0.4.0**: GridSearchCV 하이퍼파라미터 최적화
- **v1.0.0**: 최종 결과 분석 및 프로젝트 완료