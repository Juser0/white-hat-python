# White-Hat-Python

책 "화이트 해커를 위한 암호와 해킹" 을 주제로 한 CCLAB 세미나 실습 코드 저장소입니다 <br />
사용언어는 Python입니다.

## I. 암호(Cipher)

### 1장\_ 간단한 암호 도구 만들기

- 평문 (Plain Text) : 누구나 읽을 수 있고 알아볼 수 있는 문장 <br />
- 암호문 (Cipher Text) : 평문을 합당하게 푸는 방법을 모르는 사람에게 전혀 알 수 없는 형태로 변환된 문장

암호키 (Cipher Key) : 암호문 -> 평문 (해독)을 위해 사용된 방법, 줄여서 키(Key)라고 하기도 함

- 암호화 (Encryption) : 평문 -> 암호문 <br />
- 복호화 (Decryption) : 암호문 -> 평문

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

- 대칭키 암호 (Symmetric-key Cryptography) : 암호화에 사용되는 암호키 == 복호화에 사용되는 암호키인 암호화 기법 <br />
  <-> <br />
- 비대칭키 암호 (공개키 암호) : 암호화에 사용되는 암호키 != 복호화에 사용되는 암호키인 암호화 기법 (3장에서 다룰 예정)

#### 대칭키의 문제점?

- 암호키 자체는 평문이므로 분실 혹은 노출 시 해당 암호키로 암호화한 정보의 보안이 취약해짐 <br />
- 암호키를 전달하는 메커니즘이 최대의 약점이 될 수 있다 -> 송수신 측이 합의한 비밀 경로나 네트워크로 전달하는 편

#### 대칭키 암호 원리

기본적으로 XOR 연산에 기반
P XOR K = Q일 때, Q XOR K = P이다 <br />

```
P = 1 1 0 1 0 0 1 1
K = 0 1 0 1 0 1 0 1

P XOR K = Q (1 0 0 0 0 1 1 0)

Q = 1 0 0 0 0 1 1 0
K = 0 1 0 1 0 1 0 1

Q XOR K = (1 1 0 1 0 0 1 1 = P)
```

단순히 XOR 연산만으로는 너무 복호화가 쉬우므로, 실제 대칭키 암호에서는 여러 연산을 추가 <br />
대칭키 암호화 방식은 데이터 변환 방식에 따라 <br />

- 블록 암호 (Block Cipher) <br />
- 스트림 암호 (Stream Cipher) <br />
  로 나뉜다

#### 블록 암호

고정된 크기의 블록 단위로 암호화, 복호화 연산을 수행 <br />
암호키 크기에 따라 64~256비트 블록 크기로 연산을 수행 <br />
ex) DES, 3DES, AES, Blowfish, Twofish (국내 개발 : SEED, ARIA, HIGHT)

블록 암호 알고리즘은 평문을 암호 블록으로 만들 때 적용되는 방식에 따라 <br />

- 파이스텔 블록 구조 (Feistel) <br />
- SPN (Substitution-Permutation Network) 블록 구조

#### 파이스텔 블록 구조

입력되는 평문 블록을 좌우 두 개 블록으로 분할, <br />
좌측 블록은 파이스텔 함수라 불리는 라운드 함수를, <br />
우측 블록은 이를 적용하여 출력된 결과를 담는 과정을 반복적으로 수행한다

ex) DES, Blowfish, Twofish, SEED

#### SPN 블록 구조

입력되는 평문 블록을 분할하지 않고 전체 블록을 적용하는 방식 <br />
라운드 함수의 역함수를 구해야 하는 어려움이 있는 구조지만, 컴퓨팅 기술의 발전으로 어려움을 충분히 극복하였음 <br />

ex) AES, IDEA, SHARK, ARIA

#### 암호화 대상 정보 > 블록 크기인 경우

각 블록에 대해 어떤 방식으로 암호화를 수행하느냐에 따라 여러 운영모드로 나뉜다 <br />

- Electronic Codebook (ECB) <br />
- Cipher Block Chaining (CBC) <br />
- Output Feedback (OFB) <br />
- Cipher Feedback (CFB) <br />
- Counter (CTR) <br />

#### ECB mode

가장 단순한 블록암호 운영 모드 <br />
각 블록들은 암호키를 이용해 독립적으로 암호화 <br />
가장 큰 약점은 동일한 내용의 블록은 동일한 암호 블록으로 암호화 된다는 점이다 <br />
-> 만약 어떤 정보가 일정한 패턴을 가지는 경우 ECB 모드에서는 암호화하기 어려움 (특히 이미지)

#### CBC mode

블록을 암호화하기 전에 이전 블록의 암호화된 블록과 XOR 연산을 한 결과를 새로운 암호키로 하여 블록을 암호화 하는 방식 <br />
맨 첫 블록은 이전 블록이 없기 때문에 이전 블록 역할을 하는 초기화 벡터 (Initialiation Vector)가 필요

#### 스트림 암호

Binary Plain text stream, Binary key stream을 비트 단위로 XOR 연산하여 암호문을 생성 <br />
이를 위한 하드웨어 구현이 간편하고 속도가 빠르다는 점 때문에 무선통신 환경에서 무선 데이터 보호에서 사용됨 <br />
ex) RC4, / (GSM 무선통신 보안을 위한 표준) A5/1, A5/2, A5/3

#### 3DES

DES : Data Encryption Standard, 1970년대 IBM에서 파이스텔 블록 구조에 기반하여 설계되고 개발된 56 bit 비트키 암호화 알고리즘 <br />
(56bit라는 다소 크기가 작은 암호키로 인해 1999년 distributed.net에 의해 22시간 만에 깨지게 됨) <br  />

3DES : Triple DES, 블록당 3번의 DES를 수행 (168 bit의 키 암호화 알고리즘) DES에 비해 보안적 요소 증가, 성능 저하 <br />

#### AES

AES : Advanced Encryption Standard, DES를 대체하기 위해 2001년 NIST에서 제정한 새로운 암호 표준 <br />
(만든 개발자의 이름을 딴 레인달 암호화 알고리즘이라고도 함) <br />

DES와 달리 SPN 블록 구조를 채용하였고, 키는 128, 192, 256 bit 키로 암호화를 진행 <br />
완전히 해독된 사례가 없는 안전성이 보장된 알고리즘

---

### 3장\_공개키 암호 (Public-key Cryptography)

대칭키 암호의 문제점인 키의 전달에서 발생하는 취약점을 해결하고자 만들어진 암호 방식 <br />

Public key, Private key가 한 쌍으로 존재하여, <br />

- 개인키 암호화 -> 공개키 복호화 <br />
- 공개키 암호화 -> 개인키 복호화 <br />
  의 방식으로 동작합니다

그래서 공개키 암호를 비대칭키 암호라고도 부릅니다.
