arr = [1,1,3,3,0,1,1]

def solution(arr):
    for i in range(1, len(arr)-1):
        try: 
            if arr[i-1] == arr[i]:
                arr.pop(i)
            else:
                pass
        except:
            pass

    return arr


print(solution(arr))
