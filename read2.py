data = []
count = 0
data_length = 0
ave_data_lenght = 0
with open('reviews.txt', 'r') as f:
	for review in f:
		data.append(review.strip())
		count +=1
		data_length += len(review) 
		if count % 1000 == 0:
			print(len(data))
ave_data_lenght = data_length / len(data)

print('檔案讀取完成, 總共有', len(data), '筆資料')

wc = {} #word_count
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
		print('感謝使用本功能')
		break
	if word in wc:
		print(word, '出現過的次數: ', wc[word])
	else:
		primt('未查詢到此單字')