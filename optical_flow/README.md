# cv-short-projrct
## optical_flow 
画像系列からoptical flow を抽出するプログラム

### 元論文
https://www.ipol.im/pub/art/2013/26/article.pdf

### 実行ファイル
- run.py ... 実行ファイル

opt情報(x,y方向) + 白黒画像を重ねて (3,height,width) を生成  
なお，return は png ではなく .npyで保存している