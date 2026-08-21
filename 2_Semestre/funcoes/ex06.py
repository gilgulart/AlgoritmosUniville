def is_peer(num: int):
    status =  True if num % 2 == 0 else False
    return status


print(is_peer(2))
print(is_peer(3))