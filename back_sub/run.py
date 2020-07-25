"""
背景差分の情報を抽出
1. 背景差分を計算
2. 差分画像から動画を生成
"""

import argparse
import os

from background_sub import back_sub

def call_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
    parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
    parser.add_argument('-o', '--output', type=str, help='Path to a output dir', default='./output')
    args = parser.parse_args()
    return args

def main():
    args = call_argparse()
    os.makedirs(args.output, exist_ok=True)

    back_sub(args)

if __name__ == "__main__":
    main()