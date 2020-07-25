# width の比率で gif に変換
INPUT=output1/output.avi
OUTPUT=output1/output.gif
width=480

ffmpeg -i $INPUT -vf scale=$width:-1 -r 20 $OUTPUT