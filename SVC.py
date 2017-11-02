#encode: UTF-8
from sklearn import svm
import random

#2x + 3yを計算する関数
def calc(x, y):
	return 2 * x + 3 * y

#学習用データ準備
data = []
label = []
print("2x + 3y = z を学習させる")
for i in range(1000):
	#x, yは1〜10までの整数
	x = random.randint(1, 10)
	y = random.randint(1, 10)
	z = calc(x, y)
	print("x:", x, ",y:", y, "=",z)
	data.append([x, y])
	label.append(z)

#学習
clf = svm.SVC()
clf.fit(data, label)

#テスト用データ作成
testdata = []
testlabel = []
for i in range(1000):
	a = random.randint(1, 10)
	b = random.randint(1, 10)
	c = calc(a, b)
	testdata.append([a, b])
	testlabel.append(c)

#テスト用データを予測
pre = clf.predict(testdata)

#答え合わせ
ok = 0
total = 0
for idx, answer in enumerate(testlabel):
	p = pre[idx]
	if p == answer: ok += 1
	total += 1
print("正解率:", ok, "/" , total, "=", ok/total)
