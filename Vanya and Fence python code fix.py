num_friends, fence_height = map(int, input().split())  
friend_heights = list(map(int, input().split()))  

total_width = 0  

for height in friend_heights:  
    if height <= fence_height:  
        total_width += 1  
    else:  
        total_width += 2  

print(total_width)  
