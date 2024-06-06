immutable_var = 1, 2, False, "Hello"
print(immutable_var)
# immutable_var[2] = 10
print(immutable_var)  #Значение кортежа не изменяется,не поддерживает изменение элементов,при попытке изменить выдает ошибку,тем самым он занимает меньше памяти
mutable_list = ([6, 7], "World")
print(mutable_list)
mutable_list[0][0] = 9
print(mutable_list)
