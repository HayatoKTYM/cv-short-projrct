# cv-short-projrct
## optical_flow 
画像系列からoptical flow を抽出するプログラム

### 元論文
https://www.ipol.im/pub/art/2013/26/article.pdf

### 実行例
元画像は諸都合で割愛  
![image](https://user-images.githubusercontent.com/48461133/88473970-9b24a680-cf5d-11ea-8453-b3461bd0ea9d.png)

### 実行ファイル
- run.py ... 実行ファイル

opt情報(x,y方向) + 白黒画像を重ねて (3,height,width) を生成  
なお，return は png ではなく .npyで保存している
