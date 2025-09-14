# 🏠 Linear Regression 모델 최적화 프로젝트

## 📋 프로젝트 개요
California Housing Dataset을 사용한 주택 가격 예측 모델 최적화 학습 프로젝트

## 🎯 학습 목표
- 정규화(StandardScaler) 적용 효과 이해
- L1/L2 정규화(Ridge, Lasso) 비교
- GridSearchCV를 통한 하이퍼파라미터 최적화

## 📁 프로젝트 구조
```
LinearRegression/
├── data/                       # 데이터 파일들
│   └── california_housing_processed.csv  # 처리된 데이터셋
├── notebooks/                  # Jupyter notebooks
│   ├── 01_eda.ipynb           # 탐색적 데이터 분석 (한글 버전)
│   ├── 01_eda_fixed.ipynb     # 탐색적 데이터 분석 (영어/한글 호환)
│   ├── 02_normalization.ipynb # 정규화 비교 (예정)
│   ├── 03_models.ipynb        # 모델 구현 (예정)
│   ├── 04_optimization.ipynb  # 하이퍼파라미터 튜닝 (예정)
│   └── 05_analysis.ipynb      # 결과 분석 (예정)
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

### 🔄 진행 예정 단계

- [ ] **4단계: 하이퍼파라미터 최적화**
  - GridSearchCV를 통한 최적 파라미터 탐색
  - RandomizedSearchCV 비교
  - 학습 곡선 및 검증 곡선 분석

- [ ] **5단계: 결과 분석 및 시각화**
  - 최종 모델 성능 비교
  - Feature Importance 분석
  - 예측 결과 시각화

## 📈 주요 발견사항 (EDA 결과)

### 데이터셋 특성
- **데이터 크기**: 20,640개 샘플, 8개 특성
- **결측값**: 없음
- **주택 가격 범위**: $15K ~ $500K (평균: $207K)
- **지리적 분포**: 캘리포니아 전역, 해안가 지역이 상대적으로 고가

### 주요 상관관계 (타겟과의 절댓값 기준)
1. **MedInc** (중위 소득): 0.688 - 가장 강한 양의 상관관계
2. **Latitude** (위도): 0.144 - 북쪽으로 갈수록 가격 상승 경향
3. **AveOccup** (평균 거주 인원): 0.023 - 매우 약한 상관관계
4. **HouseAge** (주택 연식): 0.106 - 약한 상관관계

## 🛠️ 기술 스택
- **데이터 분석**: pandas, numpy
- **머신러닝**: scikit-learn
- **시각화**: matplotlib, seaborn, plotly
- **환경**: Python 3.13, Jupyter Notebook
- **버전 관리**: Git, GitHub

## 📝 학습 노트
- 한글 폰트 문제 해결을 위한 `font_setup.py` 모듈 개발
- matplotlib의 한글 표시 문제는 Windows 환경에서 흔히 발생
- 지리적 데이터 시각화 시 경도/위도를 활용한 산점도가 효과적
- 중위 소득(MedInc)이 주택 가격 예측에 가장 중요한 특성으로 확인