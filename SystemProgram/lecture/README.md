pip 19 최신버전은 설치에 문제가 생겨서  
pipenv run pip install pip==18.0  
이렇게 18 버전을 깔아야 한다.  
내 컴에서는
pipenv64 run pip install pip==18.0

윈도우에서 jupyter 설치 방법
- 가상환경 활성화

- > pip install jupyter matplotlib

- > jupyter notebook

- PyCharm - file - 



pycharm에서 만든 virtualenv에서 pip 버전이 낮은 경우

- C:\Users 아래 가상환경으로 들어간다.
- pip를 깔끔하게 지운다.
- C:\\Users\\goodg\\.virtualenvs\\scripts-systprog\\Scripts\\python.exe -m pip uninstall pip setuptools
- 다시 설치한다.
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- C:\\Users\\goodg\\.virtualenvs\\scripts-systprog\\Scripts\\python.exe get-pip.py