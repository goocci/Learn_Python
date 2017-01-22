# 패키지 만들기

"""
디렉토리 구조

    python(프로젝트)
        ㄴ AAA
            ㄴ BBB
                ㄴ CCC

__init__.py : 3.3 이전 버전에서는 init 파일이 없으면 패키지도 인식 안됨.
3.3 버전 부터는 init 파일이 없어도 패키지도 인식.
하위 버전과 호환을 위해서는 __init__.py 파일을 생성하는 것이 올바른 방법이다.
"""

"""
AAA
AAA.BBB
AAA.BBB.CCC

from AAA.BBB.bbb import test_bbb
import AAA.BBB.bbb
"""

# 특정 디렉토리의 모듈을 *를 이용하여 import 할 때
# 해당 디렉토리의 __init__.py 파일에 __all__이라는 변수를 설정하고
# import 가능한 모듈을 정의하면, 정의한 모듈을 import 할 수 있다.

# 1. from 패키지.패키지(폴더) import *(모듈)
#  __all__ = ['모듈명'] <-- 이렇게 정의한 모듈만 사용할 수 있다.

# 2. from 패키지.패키지.모듈 import *(여기서의 *는 모듈내에 있는 함수들을 의미)

"""
# 절대(absolute) 경로를 이용해서 지정하는 경우
from AAA.BBB.bbb import test_bbb

# 상대(relative) 경로를 이용해서 지정하는 경우 : ".."(부모폴더), "."(현재폴더)을 사용
# relative 접근자 : ".." , "." --> 모듈에서만 사용가능!! 파이썬 셀(인터프리터)에서는 사용 불가!!
from ..bbb import test_bbb
"""