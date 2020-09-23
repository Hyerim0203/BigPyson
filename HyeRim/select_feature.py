#!/usr/bin/env python
# coding: utf-8

# In[1]:


# train data feature 구성 함수


def make_data(dataset, top_code, real_weather, cat, top_real_weather, log):
    """
    인자 설명
    # topcode -> top code(True) vs top cat(False)
    # real_weather -> 실제날씨(True) vs 예보날씨(False)
    # cat -> x1_cat, x2_cat(True) vs 분류(False)
    # top_real_weather -> top_real_weather 넣을지(True), 뺄지(False)
    # log -> 판매단가, 주문량 log(True) or 안취할지(False)
    """
    
    data = dataset.copy() # 원본 데이터 수정안되게 하려고
    
    # top_code vs top_dat
    if top_code: # top code 선택(top cat 대신)
        data.drop(["top_cat"], axis=1, inplace=True)
    elif not top_code: # top cat 선택(top code 대신) 
        data.drop(["top_code"], axis=1, inplace=True)
    
    # 실제날씨vs예보날씨
    if real_weather: # 실제 날씨 선택(예보날씨 대신)
        data.drop(['예보_최고기온', '예보_최저기온', '예보_강수확률', '예보_강수량','예보_풍속'], axis=1, inplcae=True)
    elif not real_weather: # 예보날씨 선택(실제 날씨 대신)
        data.drop(['실제_최고기온', '실제_최저기온', '실제_강수량', '실제_평균풍속'], axis=1, inplace=True)
        
    # x1cat,x2cat vs 분류
    if cat: # x1_cat,x2_cat 선택
        data.drop(["분류"], axis=1, inplace=True)
    elif not cat:
        data.drop(["x1_cat","x2_cat"], axis=1, inplace=True)
        
    # top_real_weather 넣을지 말지
    if not top_real_weather:
        data.drop(["top_real_weather"], axis=1, inplace=True)
        
    # log vs 안취할지
    if log:
        data.drop(['판매단가', '주문량'], axis=1, inplace=True)
    elif not log:
        data.drop(['new판매단가','new주문량'], axis=1, inplace=True)
        
    return data

