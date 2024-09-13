# 얼굴 캐리커처 프로필 이미지 및 GIF 애니메이션 생성

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### Contents
1. <a href="#배경-및-목적">배경 및 목적</a><br>
2. <a href="#주최주관--팀원">주최/주관 & 팀원</a><br>
3. <a href="#프로젝트-기간">프로젝트 기간</a><br>
4. <a href="#프로젝트-소개">프로젝트 소개</a><br>
   4.1 <a href="#프로젝트-과정">프로젝트 과정</a><br>
   4.2 <a href="#모델-설명">모델 설명</a><br>
5. <a href="#inference">Inference</a><br>
6. <a href="#demo">Demo</a><br>
7. <a href="#발표-자료">발표 자료</a>

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### 1. 배경 및 목적
- 사람에 따라 GitHub 프로필 등 공개적인 플랫폼에 자신의 증명사진을 올리는 것이 부담스러울 수 있음
- 실제 얼굴 사진을 기반으로 사용자의 특징을 반영한 캐리커쳐를 생성하고, GIF 애니메이션으로 변환

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### 2. 주최/주관 & 팀원

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

## 3. 프로젝트 기간 
- 2024.07~ 2024.08 (2개월)

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### 4. 프로젝트 소개

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### 4.1. 프로젝트 과정
<img src="https://github.com/user-attachments/assets/ee0d41bc-7f26-451e-b2cf-f398031ebfae" width="700">

1. SAM을 사용하여 mask를 생성한다.
2. 생성된 mask 중에서 스타일 변환을 적용하고 싶은 부분의 mask만 StyleTransfer에 입력한다.
3. DiffStyler는 사용자의 얼굴 사진, 스타일 이미지과 mask를 입력받아서 스타일이 반영된 캐리커처를 생성한다.
4. Image2Video 모델인 LivePortrait에 캐리커처 이미지와 driving video를 입력하여 GIF로 변환한 최종 결과물을 출력한다. 

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### 4.2. 사용한 모델
**SAM**  
<img src="https://github.com/user-attachments/assets/2592fbc2-b439-4292-9e74-8664744d557f" width="700">

**DiffStyler**  
<img src="https://github.com/user-attachments/assets/a9087fd9-1cda-44ca-a6d5-41e207e69a56" width="700">

**Image2Video**  
<img src="https://github.com/user-attachments/assets/89968ca8-ac13-496d-8e77-96734319e067" width="700">

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

### 5. Inference

#### 5.1 모델

#### 5.2. Gradio

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

## 6. Demo

<hr style="border: 0; height: 1px; background-color: #e1e4e8;" />

## 발표 자료
