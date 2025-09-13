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
├── data/                    # 데이터 파일들
├── notebooks/              # Jupyter notebooks
│   ├── 01_eda.ipynb        # 탐색적 데이터 분석
│   ├── 02_normalization.ipynb  # 정규화 비교
│   ├── 03_models.ipynb     # 모델 구현
│   ├── 04_optimization.ipynb   # 하이퍼파라미터 튜닝
│   └── 05_analysis.ipynb   # 결과 분석
├── src/                    # Python 모듈
├── results/                # 결과 이미지, 표
├── requirements.txt
└── README.md
```

## 🚀 시작하기
1. 환경 설정
```bash
pip install -r requirements.txt
```

2. Jupyter 실행
```bash
jupyter notebook
```

## 📊 학습 단계
- [x] 프로젝트 초기 설정
- [ ] 1단계: 데이터 탐색 (EDA)
- [ ] 2단계: 정규화 효과 비교
- [ ] 3단계: 모델 구현 및 비교
- [ ] 4단계: 하이퍼파라미터 최적화
- [ ] 5단계: 결과 분석 및 시각화