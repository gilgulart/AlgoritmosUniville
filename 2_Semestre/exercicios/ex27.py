def quicksort(arr: float | int = []) -> list[float | int]:
    if len(arr) < 2:
        return arr
    
    median = len(arr) // 2
    pivot = arr[median]

    minors = [i for i in arr if i < pivot]
    big = [i for i in arr if i > pivot]
    equals = [i for i in arr if i == pivot]
    print(f"Lista atual: {arr} | Pivot: {pivot} | Minors: {minors} | Big {big}")
    return quicksort(minors) + equals + quicksort(big)

print(quicksort([10,5,2,3,55,30,20,22,9,11]))
   
   