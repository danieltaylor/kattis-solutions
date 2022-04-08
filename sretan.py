k = int(input())
k -= 1
k = str(bin(k)[2:])
k = k.replace('0', '4')
k = k.replace('1', '7')
print(int(k))
