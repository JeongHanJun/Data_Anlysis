#!/usr/bin/env python
# coding: utf-8

# ## 3. Reducing Loss (손실 줄이기)
# 
# 반복학습을 통해 손실 줄이기  
# 
# [ 초기값 - > 손실 확인, 다른 값 추정 -> 손실 확인 ] 의 반복  
#   
# 반복을 계속하면 최적의 모델에 가까워진다.  
#   
# - 그림 1. <머신러닝 알고리즘이 모델을 학습하는데 사용되는 반복적인 시행착오 과정>

# ![%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%20%EB%B0%95%EB%B3%B5%ED%95%99%EC%8A%B5.png](attachment:%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%20%EB%B0%95%EB%B3%B5%ED%95%99%EC%8A%B5.png)

# ### 반복방식의 모델 학습  
# 
# 반복 접근방식을 통해 다양한 복합적 상황, 특히 파란 먹구름안의 상황에 대해 자세히 보자.  
# 반복 전략은 주로 대규모 데이터 세트에 적용하기 용이하며, 많이 사용중이다.  
#   
#   
# 이 모델은 1개 이상의 특성을 입력하여, 하나의 예측(y′)을 출력한다.  
# 예를 들어 1개의 특성을 가지고 1개의 예측을 반환하는 모델을 생각하면

# ![image.png](attachment:image.png)

# 위에서 b 와 w₁의 초기값은 무엇으로 설정해야할까??  
#     - 선형 회귀에서는 초기값이 별로 중요하지 않다.
#     - 임의의 값을 주어도 되므로 b = 0, w₁= 0 이라는 값을 설정해보자.  
#       
# 최초 특성값(x₁) = 10이라고 가정하고, 이 특성 값을 예측 함수에 입력해보면  
#   
# y′= 0 + 0(10)  
# y′= 0  
#   
# 위 식에서 손실 계산(Loss Calculation) 은 이 모델에서 사용한 손실함수 이다.  
# 만약 제곱손실함수를 사용한다면, 손실함수는 2개의 값을 취한다.  
#   
# y′=  특성 x에 대한 모델의 예측값
# y  =  특성 x에 대한 올바른 라벨  
#   
# 이 과정을 거치고 나면, 그림1에서의 '매개변수 업데이트 계산' 과정에 도달한다.  
# 이 과정에서 손실함수의 값을 검토하여 b와 w₁의 새로운 값을 생성한다.  
#   
# 즉, 녹색상자에서 새로운 값을 생성한 다음, ML 시스템이 이러한 모든 특성을 모든 라벨과 대조하고, 재평가한다.  
# 그런 다음 손실함수의 새로운 값을 생성하여, 새 매개변수 값을 출력한다고 하면,  
#     **' 알고리즘이 손실값이 가장 낮은 모델 매개변수를 발견할 때까지 반복 학습한다. '**  
# 보통 전체 손실이 변하지 않거나, 매우 느리게 변할때까지 반복한다.  
# 이때 모델이 **수렴**했다고 말한다.

# 그림1의 녹색상자 즉 ' 매개변수 업데이트 계산 '이라는 과정을 자세하게 알아보자  
#   
# w₁이 가능한 모든 값에 대해 손실을 계산할 시간과 컴퓨팅 자료가 있다고 가정하자.  
# 회귀문제에서는 손실과 w₁을 대응한 도표는 항상 볼록모양(2차함수꼴)을 할 것이다.  
# 그래프를 대략적으로 그려보면

# ![%EA%B7%B8%EB%A6%BC2.png](attachment:%EA%B7%B8%EB%A6%BC2.png)

#         [ 그림 2. 회귀문제에서는 볼록 함수 모양의 가중치-손실 도표가 산출된다. ]  
#           
# 볼록문제에서는 기울기가 정확하게 0인 지점에 최소값이 1개 존재한다.( 이경우 극소값 = 최소값 )  
# 또한, 이 최소값에서 그래프의 기울기는 0으로 수렴하므로, 손실함수가 수렴한다고 볼 수 있다.  
#   
# 전체 데이터 세트에 대해 가능한 모든 w₁값의 손실함수를 계산하는것은 수렴 지점을 찾는데(극소값을 찾는데)굉장히 비효율적인 방법이다.  
# 이 부분에서, 머신러닝에서 널리 사용하는 **경사 하강법**이 존재한다.  
#   
# 경사하강법의 첫번째 단계는 w₁에 대한 시작 값(시작점)을 선택하는 것입니다.  
# 시작점은 별로 중요하지 않다.  
# 따라서 많은 알고리즘은 w₁을  0 혹은 임의의 값으로 설정한다.  
# 다음 그림에서는 w₁을 가시성을 위해 0보다 약간 큰 수를 지정했다.

# ![%EA%B7%B8%EB%A6%BC3.png](attachment:%EA%B7%B8%EB%A6%BC3.png)

#                            [ 그림 3. 경사하강법법의 시작점 ]  
#   
# 경사하강법은 시작점을 설정한 다음, 시작점에서 손실 곡선의 기울기를 계산합니다.  
# 즉, 기울기는 편미분의 벡터로서, 어느 방향이 더 정확한지 혹은 부정확한지 알려줍니다.  
# 그림 3에서처럼, 단일 가중치에 대한 손실의 기울기는 해당 값에서의 미분값과 같습니다.  
#   
# * 편미분과 기울기 *  
#   
#   기울기는 벡터이므로 다음 2가지 특성을 갖고 있다.  
#   + 방향  
#     
#   + 크기  
#     
# 기울기는 항상 손실 함수 값이 가장 크게 증가하는 방향을 향한다.  
# 경사하강법 알고리즘은 가능한 한 빨리 손실을 줄이기 위해 기울기의 반대방향으로 이동합니다.  

# ![%EA%B7%B8%EB%A6%BC4.png](attachment:%EA%B7%B8%EB%A6%BC4.png)

#                        [ 그림 4. 경사하강법은 음의 기울기를 사용한다. ]    
#                        
#    손실 함수 곡선의 다음 지점을 결정하기 위해 경사하강법 알고리즘은 기울기 크기의 일부를 시작점에 더한다.

# ![%EA%B7%B8%EB%A6%BC%205.png](attachment:%EA%B7%B8%EB%A6%BC%205.png)

#                [ 그림 5. 기울기 보폭을 통해 손실 곡선의 다음 지점으로 이동한다. ]  
#                  
#   그런 다음, 경사하강법은 이 과정을 반복하여 최소값에 점점 접근합니다.

# ### 3-1. 손실줄이기 - 학습률( Learning rate )  
#   
# 경사하강법 알고리즘은 기울기에 학습률 또는 보톡이라고 불리는 스칼라는 곱하여 다음 지점을 결정한다.  
# 예를들어 기울기가 2.0이고, 학습률이 0.01이면, 다음 지점은 이전 지점으로부터 기울기벡터 방향으로 0.02떨어진 지점이 된다.  
#   
# 초매개변수(HyperParameter)는 프로그래머가 머신러닝 알고리즘에서 조정하는 값이다.  
# 대부분의 경우, 프로그래머는 학습률을 미세조정하는데 상당한 시간을 소비한다.  
# 학습률을 작게 설정하면, 학습이 미세하게 진행되므로 학습시간이 매우 오래걸리게 된다.

# ![%EA%B7%B8%EB%A6%BC6.png](attachment:%EA%B7%B8%EB%A6%BC6.png)

#                     [ 그림 6. 학습률이 너무 작아서 속도가 너무 느리다. ]
#              학습률이 너무 작아서, 학습의 진행의 시간소요가 너무 크다.

# ![%EA%B7%B8%EB%A6%BC7.png](attachment:%EA%B7%B8%EB%A6%BC7.png)

#                      [ 그림 7. 학습률이 너무 커서 최소값을 지났다. ]
#             학습률이 너무 커서, 최저점을 기준으로 진동하게 되므로,  
#             이 또한 수렴하는 최소값을 찾는데에 오랜 시간이 걸린다.

# 모든 회귀에는 **골디락스 학습률**이 있다.
# 골디락스 값은 손실 함수가 얼마나 평탄한지 여부와 관련이 있다.  
# 손실함수의 기울기 값이 너무 작으면, 더 큰 학습률을 시도할 수 있다.  
# 이런식으로 기울기값을 보완하여 적절한 보폭을 만들어 낼 수 있다.

# ![%EA%B7%B8%EB%A6%BC8.png](attachment:%EA%B7%B8%EB%A6%BC8.png)

# 경사하강법(Gradient descent)에서 배치(batch)는 기울기를 계산하는 반복과정에서 사용된 예의 갯수이다.  
# 즉 batch는 모델학습의 반복1회, 경사 업데이트1회에 사용되는 예의 집합이다.  
# 위까지는 배치가 전체 데이터 세트라고 가정해왔다.  
# 하지만 실무에서 데이터는 수십억개의 너무나 많은 규모이고, 이에따라 특성x도 엄청나게 많다.  
# 따라서 배치가 너무 커질수 있다.  
# 배치가 너무 커지면, 단일 반복으로 계산하는데에도 시간이 너무 오래 걸린다.  
#   
#     
# 무작위로 샘플링한 예가 포함된 다량의 데이터에는 중복데이터가 및 NaN도 포함될 수 있다.  
# 실제로 batch_size가 커지면, 중복도 또한 올라간다.  
#   
#     
# 만약에 훨씬 적은 계산으로 적절한 기울기를 얻을 수 있다면 어떨까?  
# Dataset에서 무작위로 예를 선택했을때, 훨씬 적은 데이터 세트로 평균값을 얻을 수 있는 방법이 있다.  
# 그것을 **확률적 경사 하강법(Stochastic Gradient Descent)** 라고 한다.  
#   
# 확률적 경사 하강법(SGD)는 반복당 한의 예를 사용한다. 
# 반복이 충분하면 SGD가 효과는 있지만, 노이즈가 매우 심하다.  
# 참고로 '확률적' 이라는 단어의 의미는 각 배치를 포함하는 하나의 예가 무작위로 선출된다는 뜻이다.  
#   
# **미니 배치 확률적 경사하강법**은 전체 배치 반복과 경사하강법의 절충안이다.  
# 미니배치는 무작위로 선택한 10 ~ 1000개 사이의 예로 구성된다.  
# 미니SGD 는 SGD의 노이즈를 줄이면서도, 전체 배치보다는 더 효율적이다.  

# ![%ED%99%95%EB%A5%A0%EC%A0%81%20%EA%B2%BD%EC%82%AC%20%ED%95%98%EA%B0%95%EB%B2%95%20%ED%95%9C%EC%9E%A5%20%EC%9A%94%EC%95%BD.png](attachment:%ED%99%95%EB%A5%A0%EC%A0%81%20%EA%B2%BD%EC%82%AC%20%ED%95%98%EA%B0%95%EB%B2%95%20%ED%95%9C%EC%9E%A5%20%EC%9A%94%EC%95%BD.png)

# 위의 사진이 보기 쉽게 이 둘의 장단점을 비교해준다.  
# (배치)경사 하강법은  다음 원을 위해 현재 원의 모든 점을 다 계산한다. 그리고 그중 최적의 점을 찾는 이 과정을 반복한다.  
# 확률적 경사하강법은 한원에서의 모든 점을 계산하지 않고, 일부 점들을 무작위로 추출한다. 이 일부 점들의 집합이 Mini_Batch 이다. 초기 원에서는 미니배치를 사용한 기울기(Gradient) 즉 SGD 가 BGD보다 부정확한다. 하지만 계속 이 과정이 진행되면서 점점 SGD는 BGD보다 목표에 수렴해진다. 결국 최종적으로 도달했을때는 BGD와 SGD의 결과값 차이가 거의 없다는 것이다.  
# 
# 이를 말하는 내용이 위 사진의 오른쪽 하단의 설명인  
# **Local Minima 보다 Global Minima에 수렴할 가능성이 더 높다.** 이다.  
# 사실상 우리의 목표는 결과값이 목표치에 가까울수록 좋은것이다.  
# 결과값에 거의 차이가 없다면, 속도가 더 빠른 SGD가 선호되는것이다.  
# 추가적으로 만약, 어떤 반복 단계에서 잘못된 방향으로 나아갔다면 BGD는 이것을 그대로 따라가므로 이 실수를 복구할 수 없다.  
# 하지만 SGD는 항상 해당원에서 최적의 해답을 찾아가므로, 이 실수를 극복할 확률도 높다는 장점이 있다.  

# [ 이쯤에서 다시 이전학습의 내용을 간략히 복습해보면 ]
# 1. 지도 학습(Supervised Learning)  
# 
#     **특정 입력(Input)에 대하여 올바른 정답(Right Answer)이 있는 데이터 집합이 주어지는 경우의 학습** 
#     
#     Input과 Output에 대한 관계를 유추하여 올바른 해답(Right Answers)을 제시  
#     
#     
#     - 회귀분석(Regression)  
#         - 연속적인 값을 찾는 것
#         - Input에 대응하는 Output을 분석하여 연속함수를 찾는 과정  
#       
#     - 분류(Classification)  
#         - Input에 대응하는 Output을 분석하여 Discrete(이산적인) 값을 찾는 것  
#         - 학습 알고리즘(Learning Algorithm)이 많은 특징들(Features)을 다룰 수 있다는 것  
#           
# 2. 비지도 학습(Unsupervised Learning)  
# 
#     **특정 입력(Input)에 대하여 올바른 정답(Right Answer)이 없는 데이터 집합이 주어지는 경우의 학습**  
#       
#     Input이 Output에 대한 Right Answer을 가지고 있지 않을 때, Data Set를 Cluster로 분리하는 학습  
#       
#     Unsupervised Learning은 Supervised Learning과 다르게 Right Answer이 주어지지 않습니다. 
#         ( 비지도학습은 지도학습과 다르게 정답 및 예에 대한 Label이 주어지지 않는다. )    
#         
#     잘못된 Prediction Result에 대해서 Feedback을 받고 교정을 할 수 없습니다.  

# ### 실습 - Reducing Loss  - 플레이그라운드 실습
#   
# * 각 플레이그라운드 실습에서는 데이터 세트를 생성한다.  
# * 생성된 데이터 세트의 라벨에는 2가지 값이 저장 가능하다.  
# * 가능한 2가지 값을 Spam(쓰레기) vs Non-Spam(쓰레기 아닌 것) 혹은 Healthy vs Sick 처럼 구분할 수 있다.  
# * 실습의 목표 :  다양항 초매개변수(Hyperparameter)를 조정하여 각 라벨값을 서로 올바르게 분리 혹은 구분하는 모델을 만드는 것을 목표로 한다.  
# * 대부분의 데이터세트는 노이즈를 포함한다. 따라서 모든 예를 명확하게 구분하는것은 불가능하다.(실전에서도 이러하다)

# ![%EC%8B%A4%EC%8A%B5%20%EC%8B%9C%EA%B0%81%ED%99%94.png](attachment:%EC%8B%A4%EC%8A%B5%20%EC%8B%9C%EA%B0%81%ED%99%94.png)

# < 위 그림은 실습 모델의 시각화를 보여준 것이다 >  
# * 참고사항*  
#     - 각 파란색 점은 한 데이터 클래스(예: 건강한 나무)의 한 가지 예를 나타낸다.  
#       
#     - 각 주황색 점은 다른 데이터 클래스(예: 병든 나무)의 한 가지 예를 나타낸다.  
#       
#     - 배경 색상은 모델이 예측한 해당 색상 예의 위치를 나타냅니다.  
#       파란색 점 주위의 파란색 배경은 모델이 해당 예를 올바로 예측하고 있음을 의미합니다.  
#       이와 반대로 파란색 점 주위의 주황색 배경은 모델이 해당 예를 잘못 예측하고 있음을 의미합니다.  
#         
#     - 파란색과 주황색 배경은 농도가 조정됩니다.  
#       예를 들어 시각화의 왼쪽은 완전히 파란색이지만 시각화의 중심으로 갈수록 점점 흰색이 됩니다.  
#       색상 농도는 모델이 얼마나 확실하게 추측하는지를 나타내는 것으로 간주할 수 있습니다.  
#       따라서 짙은 파란색은 모델이 매우 확실하게 추측한다는 것을 의미하며 옅은 파란색은 모델이 덜 확실하게 추측한다는 것을 의미합니다.  
#       그림에 표시된 모델 시각화는 데이터를 효과적으로 예측하지 못합니다.  

# ![%EC%8B%A4%EC%8A%B5%20%EC%B4%88%EA%B8%B0%ED%99%94%EB%A9%B4.png](attachment:%EC%8B%A4%EC%8A%B5%20%EC%B4%88%EA%B8%B0%ED%99%94%EB%A9%B4.png)

#                                            [ 실습 초기화면 ]

# ![%EC%8B%A4%EC%8A%B5%201%EB%B2%88%20%EB%B0%98%EB%B3%B5.png](attachment:%EC%8B%A4%EC%8A%B5%201%EB%B2%88%20%EB%B0%98%EB%B3%B5.png)

#                                         [ 실습 1번 반복 ]

# ![%EC%8B%A4%EC%8A%B5%203%EB%B2%88%EB%B0%98%EB%B3%B5.png](attachment:%EC%8B%A4%EC%8A%B5%203%EB%B2%88%EB%B0%98%EB%B3%B5.png)

#                                            [ 실습 3번 반복 ]

# ![%EC%8B%A4%EC%8A%B5%2010%EB%B2%88%20%EB%B0%98%EB%B3%B5.png](attachment:%EC%8B%A4%EC%8A%B5%2010%EB%B2%88%20%EB%B0%98%EB%B3%B5.png)

#                                         [ 실습 10번 반복 ]

# ![%EC%8B%A4%EC%8A%B5%2050%EB%B2%88%20%EB%B0%98%EB%B3%B5.png](attachment:%EC%8B%A4%EC%8A%B5%2050%EB%B2%88%20%EB%B0%98%EB%B3%B5.png)

#                                        [ 실습 50번 반복 ]

# #### 실습의 결론  
# - 파란점의 분포는 좌vs우 기준 우측이 더 많고, 상vs하 기준 상측에 더 많다.    
# - 결국 이 실습모델의 라벨을 구분짓는 선은 시계기준 11시-5시를 잇는 직선이 된다.
# - 실습률을 3으로 설정했지만, 10으로 설정하면 더욱더 급격하게 변한다. ( 11-5 직선을 기준으로 좌우로 진동한다)  
# - 실습률은 0.1로 설정하면, 아주 미세하게 변화하며, 50번을 돌려도 11-5 직선이 답이 된다는 확신이 없다.  
# - 실습률은 적당히 3정도로 설정하고, 10번정도 진행하면 대략적인 흐름의 파악으로 수렴 과정을 파악할 수 있다.  
# - 따라서, 실습률을 적당한 값으로 설정하는것이 매우 중요하다.

# In[ ]:




