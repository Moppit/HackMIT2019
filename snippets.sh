./muse-io --osc osc.tcp://localhost:5000 --device call

./muse-player -l 5000 -C /tmp/out.csv

ffmpeg -i in out