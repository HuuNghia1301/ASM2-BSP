arr = [100, -123, 0, 1, 1, 22, 3, -3214, 132, 3, 51, 7, -1]

# for i in arr:
    # if i % 2 != 0:
        # print(f"{i} la so le")
        # 
# for a in arr:
    # if a % 6 == 0:
        # print(f"{a} chia het cho 6")

import math

for i in arr:
    x = i > 0 and int(math.sqrt(i))
    if x*x == i:
        print(i)
        

        
    
        
