## Linux Installation

1. Install VirutalBox
    - Visit https://www.virtualbox.org/wiki/Downloads
    - Download "WIndows Hosts"
    - Install it

2. Create Ubuntu Image
    - Visit http://releases.ubuntu.com/16.04/
    - Download "ubuntu-16.04.5-desktop-amd64.iso "
    - Start VirtualBox
    - Click "새로 만들기"
    - Name a new machine as *Ubuntu16*
    - Set memory size as 2048MB
    - Proceed by "yes-yes-yes"
    - Set disk size as 15GB
    - Check if "Ubuntu16" was created in VirtualBox

3. Install Ubuntu
    - Start *Ubuntu16*
    - Set language as "English"
    - Set user name as you want but **fix password as "ei316"**
    - Don't let computer name to be longer than 5 letters
    - After installation, restart the machine

4. Install Hangul
    - refer to [link1](http://androidtest.tistory.com/52) or [link2](https://m.blog.naver.com/PostView.nhn?blogId=opusk&logNo=220986268503&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F)

5. Install qt
    - Visit https://download.qt.io/archive/qt/5.11/5.11.1/
    - Install it by double click

6. Additional settings
    - 외부 USB 연결
        - [여기](https://www.virtualbox.org/wiki/Downloads) 
        에서 다운로드 후 설치: "VirtualBox Extension Pack"
        - 가상 머신 시작
        - "장치" - "게스트 확장 CD 이미지 삽입" 후 설치
        - 가상 머신 재시작
        - "장치" - "USB" - 연결할 USB 선택
    - host PC와 공유 폴더 설정
        - 외부 USB 설정처럼 설치
        - VirtualBox에서 "설정" - "공유폴더" - "머신폴더" 아래에 공유할 폴더 선택 
        - 재시작
    - 시스템이 너무 느릴 때
        - VirtualBox 실행
        - 가상머신 우클릭 - "설정" - "시스템" - "프로세서" 에서 프로세서 개수 할당

