#  Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result.
# For eg.
# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 
# (1*5, 1*5+5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)
# output-(5, 40, 91, 136, 80)


tpl = (1, 5, 7, 8, 10)
length = len(tpl)
result = []
for i in tpl:
    if tpl.index(i) == 0:
     result.append(i * tpl[1])
    elif tpl.index(i) == length - 1:
       result.append(i * tpl[-2])
    else:
       result.append(i * tpl[tpl.index(i) - 1] + i * tpl[tpl.index(i) + 1])

result = tuple(result)
print(result)