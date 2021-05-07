import os
import glob

# 특정 디렉터리의 모듈을 *를 이용하여 import할 때에는 아래와 같이 해당 디렉터리의 __init__.py 파일에 __all__이라는 변수를 설정해야 import 할수 있음
__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
