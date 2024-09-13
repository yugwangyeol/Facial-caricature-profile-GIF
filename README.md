# 얼굴 캐리커처 프로필 이미지 및 GIF 애니메이션 생성
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


## 1. 배경 및 목적


- 사람에 따라 GitHub 프로필 등 공개적인 플랫폼에 자신의 증명사진을 올리는 것이 부담스러울 수 있다. 
- 실제 얼굴 사진을 기반으로 사용자의 특징을 반영한 캐리커쳐를 생성하고, GIF 애니메이션으로 변환한다.


## 2. 주최/주관 & 팀원

- 주최/주관 : 국민대학교 AI빅데이터융합경영학과 인공지능 학회 X:AI

- 총 5인 [권민지, 김서령, 김진하. 유광열(팀장), 조현식]


## 3. 프로젝트 기간 

- 2024.07~ 2024.08 (2개월)


## 4. 프로젝트 소개

### 4.1. 프로젝트 과정

<img src="https://github.com/user-attachments/assets/ee0d41bc-7f26-451e-b2cf-f398031ebfae" width="700">

1. SAM을 사용하여 mask를 생성한다.
2. 생성된 mask 중에서 스타일 변환을 적용하고 싶은 부분의 mask만 StyleTransfer에 입력한다.
3. DiffStyler는 사용자의 얼굴 사진, 스타일 이미지과 mask를 입력받아서 스타일이 반영된 캐리커처를 생성한다.
4. Image2Video 모델인 LivePortrait에 캐리커처 이미지와 driving video를 입력하여 GIF로 변환한 최종 결과물을 출력한다. 


### 4.2. 사용한 모델

**SAM**  
<img src="https://github.com/user-attachments/assets/2592fbc2-b439-4292-9e74-8664744d557f" width="700">

**DiffStyler**  
<img src="https://github.com/user-attachments/assets/a9087fd9-1cda-44ca-a6d5-41e207e69a56" width="700">

**Image2Video**  
<img src="https://github.com/user-attachments/assets/89968ca8-ac13-496d-8e77-96734319e067" width="700">


## 5. Inference
1. git clone
```
git clone https://github.com/yugwangyeol/2024_XAI_ADV_CV1_Toyproject.git
```

2. 필요한 패키지를 다운로드 해주세요.
```
cd 2024_XAI_ADV_CV1_Toyproject
pip install git+https://github.com/facebookresearch/segment-anything.git
pip install gradio

# DiffStyler
cd DiffStyler
pip install -r requirements.txt
pip install "jax[cuda12_pip]==0.4.23" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

# LivePortrait
cd ../LivePortrait
pip install -r requirements.txt
cd ../
```

3. 아래 코드를 실행하면 Gradio가 실행됩니다.
```
python main.py
```
- Colab 환경에서는 `Gradio_main.ipynb` 파일을 실행하여, 코드를 차례대로 실행하면 됩니다.
  
## 6. Demo


## 발표 자료
[X:AI ADV CV1팀 Toy Project 중간발표,pdf](https://github.com/yugwangyeol/2024_XAI_ADV_CV1_Toyproject/발표자료
/XAI_CV_Toy_project_중간발표.pdf)
[X:AI ADV CV1팀 Toy Project 최종발표,pdf](https://github.com/yugwangyeol/2024_XAI_ADV_CV1_Toyproject/발표자료
/XAI_CV_Toy_project_최종발표.pdf)

