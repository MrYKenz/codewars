def delete_nth(order, max_e):
    new_array = []
    for i in order:
        if new_array.count(i) < max_e:
            new_array.append(i)
    return new_array
    
print(delete_nth([1,1,1,1], 2))
