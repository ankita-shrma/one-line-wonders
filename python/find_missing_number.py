print(max(arr) + 1 if arr == list(range(min(arr), max(arr) + 1)) else [i for i in range(min(arr),max(arr) + 1) if i not in arr][0] if arr != range(min(arr),max(arr) + 1) else max)