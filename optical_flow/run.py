"""
optical flow を抽出するプログラム
x,y 方向 + 白黒画像を重ねて3ch で保存
input は 画像系列なのでそれらを含むdirectoryを指定する
"""
import argparse
import os
import glob
import numpy as np

from make_opt import make_flow

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='specify input img dir')
    parser.add_argument('--flow_only', action='store_true')
    parser.add_argument('-o', '--output', type=str, help='output directory')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    img_path_list = sorted(glob.glob(os.path.join(args.input,'*png')))
    # make flow
    x_flow = make_flow(img_path_list, flow_only=args.flow_only)
    # save 
    for i in range(len(img_path_list)):
        path = os.path.basename(img_path_list[i]).replace('.png','.npy')
        output = os.path.join(args.output, path)
        print(output)
        np.save(output, x_flow[i])
    else:
        finish = True
    print('generated successfully') if finish else print('runtime error')

if __name__ == '__main__':
    main()