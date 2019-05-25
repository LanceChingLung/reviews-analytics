# 讀取檔案

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
print('平均每筆資料長度:', ave_data_lenght)
