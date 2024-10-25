
# 📄 Introduction

노마드 코더에서 진행하는 파이썬 10주 스터디의 팀 프로젝트 **PdfChatbot App**의 
백엔드(API SERVER) 입니다.

Frontend Repository: [pdf-chatbot-front](https://github.com/LikeRudin/pdf-chatbot-front)

---

## 🚀 Features

1일차 과제 
- 🔒 **User Authentication**: 로그인, 로그아웃, 회원가입.
---

## 🛤️ API Endpoints

### **Authentication**

| Method | URI                         | Description        |
|--------|-----------------------------|--------------------|
| `POST` | `/api/v1/users/login`        | 사용자 로그인       |
| `POST` | `/api/v1/users/logout`       | 사용자 로그아웃      |
| `POST` | `/api/v1/users/join`         | 사용자 회원가입  |

2 번쨰 과제

### 📜 **Conversations**

| URI                         | Description        |
|-----------------------------|--------------------|
| `/api/v1/conversations/`   | 새로운 대화생성     |
| `/api/v1/messages/`         |메시지 Read, Create |


-> 실제 구현내용

| Method | URI                         | Description        |
|--------|-----------------------------|--------------------|
| `GET` |  `/api/v1/conversations/`        | 사용자의 채팅방 목록 조회 |
| `POST` | `/api/v1/conversations/`        | 새로운 채팅방 생성   |
| `GET` | `/api/v1/conversations/pk/messages`        | 채팅방의 메시지 조회 |
| `POST` |  `/api/v1/conversations/pk/messages`        |채팅방의 메시지 생성 |

3 번째 과제

### 🗝️ **API Keys**


| Method | URI                         | Description        |
|--------|-----------------------------|--------------------|
| `GET` |  `/api/v1/keys/`        | 사용자의 api key 목록 조회|
| `POST` | `/api/v1/keys/`        | 새로운 api key 등록  |
| `Delete` | `/api/v1/keys/pk/`        | api key 삭제 |
|`Get`| `/api/v1/keys/pk/statics`| api key 사용량 조회 |

API Key를 선택하는 기능을 만들었습니다.
신용카드처럼 여러개를 등록할 수있게 하기위해서입니다.
하지만 아직 open ai의 apikey만 검증하여 등록할 수있습니다.
통계와 비용분석 api는 형태만 만들어놨습니다..

---

## 🛠️ Stacks



| Tech           | 
|----------------|
|**Python** |
| **Django**     | 
| **DRF**        |       
| **JWT**        | 
| **PostgreSQL** | 

---


## 📋 Response JSON Format

프론트엔드 개발자가 편하게 이용할 수있도록 
API가 반환하는 객체의 타입을 다음으로 통일하였습니다.


```json
{
  "success": boolean, // 유저가 신청한 작업의 성공여부
  "message": "string",   // 서버에서 보내는 요청에 관한 메시지 
  "data": null,  // 서버에서 전송하는 데이터
  "errors": {} // 서버에서 개발자에게 전송하는 에러 메시지
}
```

---

## 📦 Deployment

backend server: 아직 로컬에서만 작업중입니다.
- **HostPythonAnywhere** 이용 예정

db: superbase postgresql storage


---


## 🛡️ License

MIT

---
