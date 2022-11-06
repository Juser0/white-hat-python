# White-Hat-Python

책 "화이트 해커를 위한 암호와 해킹" 을 주제로 한 CCLAB 세미나 실습 코드 저장소입니다
사용언어는 Python입니다.

## I. 암호(Cipher)

### 1장\_ 간단한 암호 도구 만들기

- 평문 (Plain Text) : 누구나 읽을 수 있고 알아볼 수 있는 문장 <br />
- 암호문 (Cipher Text) : 평문을 합당하게 푸는 방법을 모르는 사람에게 전혀 알 수 없는 형태로 변환된 문장

암호키 (Cipher Key) : 암호문 -> 평문 (해독)을 위해 사용된 방법, 줄여서 키(Key)라고 하기도 함

- 평문 -> 암호문 (암호화 Encryption) <br />
- 암호문 -> 평문 (복호화 Decryption)

#### 암호와 코드의 차이

코드(부호) (code) : 대중에게 변환 규칙을 공개하여 어느 누구나 해독할 수 있도록 만들어놓은 기호 표시 방법 <br />
#ex) 모스 부호, 유니코드, ASCII 코드

디코딩 (Decoding) : 코드를 문자나 숫자로 변환 <br />
인코딩 (Encoding) : 문자나 숫자를 코드로 변환

#### 파이썬 기초 중 기록할 만한 내용

파일 입출력
open(filepath, readtype) <br />
r = read / w = write / a = add <br />
t = txt mode / b = binary mode <br />
'+' = open option

ex) file = open(filepath, 'wb+') <br />
-> binary, write mode file make and open

file.read() <br />
-> return file all text

file.write(content) <br />
-> write content in file

---

### 2장\_대칭키 암호 (Symmetric-key Cryptography)
