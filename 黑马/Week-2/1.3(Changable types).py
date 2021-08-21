                                # Changable types 可变类型: List , Dict, Set
a = [10, 20]
b = a

print(b)  # [10,20]

print(id(a))    # 1563466679872
print(id(b))    # 1563466679872

a.append(30)

print(b)        # [10,20,30]  是可变类型，so 随着 a 变了

print(id(a))    # 1563466679872
print(id(b))    # 1563466679872
