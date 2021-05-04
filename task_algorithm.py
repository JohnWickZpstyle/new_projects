n = 7
list_chr = [[j for j in ["."] * n ] for i in range(n)]

for i in range(len(list_chr)):
    for j in range(len(list_chr)):
        #print(list_chr[i][j], end=' ')
        if j == (n - 1)// 2:
            list_chr[i][j] = "*"
        elif i == (n - 1)// 2:
            list_chr[i][j] = "*"
        elif j == i:
            list_chr[i][j] = "*"
        elif i + j == len(list_chr) - 1:
            list_chr[i][j] = "*"
for a in list_chr:
    for b in a:
        print(b,end =' ')
    print()
