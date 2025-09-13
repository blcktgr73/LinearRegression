"""
한글 폰트 설정을 위한 유틸리티 모듈
matplotlib에서 한글을 제대로 표시하기 위한 설정
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import warnings
import os

def setup_korean_font():
    """한글 폰트 설정"""

    # 시스템별 한글 폰트 목록
    korean_fonts = []

    if platform.system() == 'Windows':
        korean_fonts = [
            'Malgun Gothic',  # 맑은 고딕
            'Microsoft YaHei',
            'NanumGothic',
            'Arial Unicode MS'
        ]
    elif platform.system() == 'Darwin':  # macOS
        korean_fonts = [
            'AppleGothic',
            'Arial Unicode MS',
            'NanumGothic'
        ]
    else:  # Linux
        korean_fonts = [
            'NanumGothic',
            'DejaVu Sans'
        ]

    # 사용 가능한 폰트 찾기
    available_fonts = [f.name for f in fm.fontManager.ttflist]

    selected_font = None
    for font in korean_fonts:
        if font in available_fonts:
            selected_font = font
            break

    if selected_font:
        plt.rcParams['font.family'] = selected_font
        print(f"✅ 한글 폰트 설정 완료: {selected_font}")
    else:
        # 한글 폰트가 없으면 영어로 표시하도록 설정
        plt.rcParams['font.family'] = 'DejaVu Sans'
        print("⚠️  한글 폰트를 찾을 수 없습니다. 영어로 표시됩니다.")

    # 음수 기호 깨짐 방지
    plt.rcParams['axes.unicode_minus'] = False

    return selected_font

def get_safe_title(korean_title, english_title):
    """한글 폰트 사용 가능 여부에 따라 적절한 제목 반환"""
    try:
        # 현재 폰트로 한글 렌더링 테스트
        fig, ax = plt.subplots(figsize=(1,1))
        ax.text(0.5, 0.5, '테스트', fontsize=10)
        plt.close(fig)
        return korean_title
    except:
        return english_title

# 폰트 설정 실행
if __name__ == "__main__":
    setup_korean_font()

    # 테스트
    plt.figure(figsize=(8, 6))
    plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
    plt.title('한글 테스트 - Korean Font Test')
    plt.xlabel('X축')
    plt.ylabel('Y축')
    plt.show()