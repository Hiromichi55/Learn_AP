with open('a.txt', 'r') as file:
    data = file.read()
result = []
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data = data.splitlines("¥n")

# 削除対象の記号
remove_chars = ['•', '・', '.', '*']
for i in data:
    # 指定した記号を削除
    for ch in remove_chars:
        i = i.replace(ch, "")
    if any(str(num) in i for num in a):
        # 数字が含まれていたら数字だけ削除
        for num in a:
            i = i.replace(str(num), "")
        if i.strip() != "":
            result.append(i)
    else:
        if i.strip() != "":
            result.append(i)

for i in result:
    if i.strip() != "":
        print(f"### {i}")