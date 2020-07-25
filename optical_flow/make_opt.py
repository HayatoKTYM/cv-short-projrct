__author__ = 'Hayato Katayama'
__date__ = '20191106'

import numpy as np
import cv2
import math
from skimage.color import rgb2gray
from skimage.registration import optical_flow_tvl1

"""
画像をresizeするプログラム & 保存
default は (224,224,3)
学習に使う画像を生成する
"""

def make_flow(img_path_list, flow_only=False):
    """
    渡された画像pathに対してflow を計算する (2,224,224)
    gray 画像と 統合して、 (3,224,224) で返す

    2020/06/15: 追加 flow_only(=False)
    gray 画像を統合せずに (2,224,224) で返す
    """
    flow_list = []
    # 1毎目は差分なし
    img = cv2.imread(img_path_list[0])
    x = np.zeros((2,img.shape[0],img.shape[1]))

    if not flow_only:
        x = np.append(x,np.expand_dims(rgb2gray(img),axis=0),axis=0)
        # print(rgb2gray(img))
        exit()
    flow_list.append(x)        
    for i in range(1,len(img_path_list)):
        img_pre = cv2.imread(img_path_list[i-1])
        img = cv2.imread(img_path_list[i])
        flow = optical_flow_tvl1(rgb2gray(img), rgb2gray(img_pre))
        if not flow_only:
            flow = np.append(flow,np.expand_dims(rgb2gray(img),axis=0),axis=0)
        flow_list.append(flow) 
    return flow_list
