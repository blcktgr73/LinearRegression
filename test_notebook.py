#!/usr/bin/env python3
"""
Jupyter 노트북 테스트 스크립트
이 스크립트는 노트북의 모든 셀을 순차적으로 실행하여 오류가 있는지 확인합니다.
"""

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import sys
import os

def test_notebook(notebook_path):
    """노트북을 실행하고 테스트하는 함수"""

    print(f"📓 노트북 테스트 시작: {notebook_path}")
    print("=" * 50)

    try:
        # 노트북 파일 읽기
        with open(notebook_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)

        # ExecutePreprocessor 설정
        ep = ExecutePreprocessor(
            timeout=600,  # 10분 타임아웃
            kernel_name='python3',
            allow_errors=False  # 오류 발생 시 중단
        )

        # 노트북 실행
        print("🔄 노트북 실행 중...")
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})

        print("✅ 노트북 실행 완료! 모든 셀이 성공적으로 실행되었습니다.")

        # 셀별 실행 결과 요약
        cell_count = len(nb.cells)
        code_cells = sum(1 for cell in nb.cells if cell.cell_type == 'code')

        print(f"\n📊 실행 결과 요약:")
        print(f"   • 전체 셀 수: {cell_count}")
        print(f"   • 코드 셀 수: {code_cells}")
        print(f"   • 마크다운 셀 수: {cell_count - code_cells}")

        return True

    except Exception as e:
        print(f"❌ 노트북 실행 중 오류 발생:")
        print(f"   오류 내용: {str(e)}")
        print(f"   오류 타입: {type(e).__name__}")
        return False

def main():
    """메인 함수"""
    notebook_path = "notebooks/01_eda.ipynb"

    if not os.path.exists(notebook_path):
        print(f"❌ 노트북 파일을 찾을 수 없습니다: {notebook_path}")
        sys.exit(1)

    success = test_notebook(notebook_path)

    if success:
        print("\n🎉 테스트 성공!")
        sys.exit(0)
    else:
        print("\n💥 테스트 실패!")
        sys.exit(1)

if __name__ == "__main__":
    main()