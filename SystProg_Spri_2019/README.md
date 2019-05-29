윈도우에서 jupyter 설치 방법
- 가상환경 활성화

- > pip install jupyter matplotlib

- > jupyter notebook


pycharm에서 만든 virtualenv에서 pip 버전이 낮은 경우

- C:\Users 아래 가상환경으로 들어간다.
- pip를 깔끔하게 지운다.
- C:\\Users\\goodg\\.virtualenvs\\scripts-systprog\\Scripts\\python.exe -m pip uninstall pip setuptools
- 다시 설치한다.
- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
- C:\\Users\\goodg\\.virtualenvs\\scripts-systprog\\Scripts\\python.exe get-pip.py
- 그랬더니 시스템 기본 pip가 이렇게 바뀐다.

```
$ pip --version
pip 19.1.1 from C:\Users\goodg\AppData\Roaming\Python\Python36\site-packages\pip (python 3.6)
```

- 하지만 잘되고 기존에 pipenv 문제도 해결됐다.