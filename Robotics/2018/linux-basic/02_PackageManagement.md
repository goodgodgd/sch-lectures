# Package Management

### apt 명령어 용법

패키지 업데이트, 목록
```
# 저장소 패키지 목록 업데이트
$ sudo apt update

# 설치된 패키지 최신 버전 업그레이드
$ sudo apt upgrade

# 시스템 커널까지 업그레이드 (오래 걸림)
$ sudo apt full-upgrade

# 설치된 패키지 목록
$ sudo apt list --installed

# 업그레이드 가능한 패키지 목록
$ sudo apt list --upgradable
```

패키지 검색
```
# 패키지 저장소의 패키지 검색
$ sudo apt search [package name or pattern]
$ sudo apt search unity-tweak-*

# 설치된 패키지 검색
$ sudo list --installed [package name or pattern]
$ sudo list --installed gedit*
> Listing... Done
  gedit/xenial,now 3.18.3-0ubuntu4 amd64 [installed]
  gedit-common/xenial,xenial,now 3.18.3-0ubuntu4 all [installed]
```

패키지 설치 및 삭제
```
# 패키지 설치 (예시: unity-tweak-tool)
$ sudo apt install [package1] [package2]
$ sudo apt install unity-tweak-tool

# 패키지 삭제
$ sudo apt remove [package1] [package2]
$ sudo apt remove unity-tweak-tool

# 패키지 완전 삭제 (설정파일까지 삭제)
$ sudo apt purge [package1] [package2]

# 패키지 삭제 후에는 쓰이지 않게된 의존 패키지들을 삭제한다.
$ sudo apt autoremove
```

저장소 추가
```
# atom editor 설치 예시
$ sudo add-apt-repository ppa:webupd8team/atom
$ sudo apt update; sudo apt install atom
```

