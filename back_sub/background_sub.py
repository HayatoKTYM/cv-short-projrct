"""
背景差分の情報を抽出
1. 背景差分を計算
2. 差分画像から動画を生成
"""
import cv2 as cv
import os

def back_sub(args):
    if args.algo == 'MOG2':
        backSub = cv.createBackgroundSubtractorMOG2(history = 1000, varThreshold = 100)
    else:
        backSub = cv.createBackgroundSubtractorKNN(dist2Threshold = 400.0)
    
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(3,3))
    capture = cv.VideoCapture(cv.samples.findFileOrKeep(args.input))
    fps = capture.get(cv.CAP_PROP_FPS)
    print('fps:',fps)

    if not capture.isOpened:
        print('Unable to open: ' + args.input)
        exit(0)
    cnt = 0
    
    while True:
        ret, frame = capture.read()
        if frame is None:
            break
        elif cnt == 0:
            h, w = frame.shape[:2]
            print('height:',h)
            print('width:',w)
            # exit()
            fourcc = cv.VideoWriter_fourcc("M","J","P","G")
            #fourcc = cv.VideoWriter_fourcc(*'XVID')
            out = cv.VideoWriter(os.path.join(args.output, 'output.avi'),fourcc, fps, (w,h), False)
        cnt += 1
        fgMask = backSub.apply(frame)
        print(fgMask.shape)
        #exit()
        cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
        cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
                cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
        out.write(fgMask)
        #cv.imwrite('./{}.png'.format(str(cnt).zfill(6)),fgMask)
        print(cnt)
        keyboard = cv.waitKey(30)
        if keyboard == 'q' or keyboard == 27:
            break
    out.release()