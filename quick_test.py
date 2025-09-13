#!/usr/bin/env python3
"""
노트북 빠른 테스트 스크립트
"""

import subprocess
import sys
import os

def quick_test_notebook(notebook_path):
    """nbconvert를 사용한 빠른 노트북 테스트"""

    print(f"🚀 빠른 노트북 테스트: {notebook_path}")

    try:
        # nbconvert로 노트북 실행 (출력은 생성하지 않음)
        result = subprocess.run([
            'jupyter', 'nbconvert',
            '--to', 'notebook',
            '--execute',
            '--stdout',
            notebook_path
        ], capture_output=True, text=True, cwd=os.getcwd())

        if result.returncode == 0:
            print("✅ 노트북이 성공적으로 실행되었습니다!")
            return True
        else:
            print("❌ 노트북 실행 실패:")
            print(result.stderr)
            return False

    except Exception as e:
        print(f"❌ 오류 발생: {e}")
        return False

if __name__ == "__main__":
    success = quick_test_notebook("notebooks/01_eda.ipynb")
    sys.exit(0 if success else 1)