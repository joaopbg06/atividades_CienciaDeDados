x = ['item0','item1','item2', 'item3','item4' ]

# Leitura

print(x)
print(x[2])
print(len(x))

# Alteração

x[2] = 'item2Mod'
print(x[2])
print(x)

# Adicionar - append

x.append('item5')
print(x[5])
print(x)

# Adicionar - insert

x.insert(0, 'itemAdicional')
print(x)

# Remover - remove

x.remove('itemAdicional')
print(x)

# Remover - pop

x.pop(5)
print(x)

# min / max

y = [ 12, 55, 23, 65, 1, 5, ]

print(max(y))
print(min(y))

