name = ['Thomas H.Cormen', 'Charles E.Leiserson', 'Ronald L.Rivest']
print('I want to invite ' + name[0] + ', ' + name[1] + ' and ' + name[2] + ' for dinner.')
print(name[2] + " can't come to my dinner.")
name[2] = 'Clifford Stein'
print('I invite ' + name[2] + ' instead.')
print('I want to invite ' + name[0] + ', ' + name[1] + ' and ' + name[2] + ' for dinner.')
print('I just find a larger table for dinner, so I want to invite three persons more for dinner.')
name.insert(0, 'Josiah L. Carlson')
name.insert(2, 'Aravind Shenoy')
name.append('Ulrich Sossou')
print('I want to invite ' + name[0] + ', ' + name[1] + ', ' + name[2] + ', ' + name[3] + ', ' + name[4] + ', ' + ' and ' + name[5] + ' for dinner.')
print("I'm sorry to tell you that the larger table I just find can't be sent in time, so I can only invite two persons for dinner")
print(name.pop() + ", I'm very sorry to tell you that I can't invite you for dinner.")
print(name.pop() + ", I'm very sorry to tell you that I can't invite you for dinner.")
print(name.pop() + ", I'm very sorry to tell you that I can't invite you for dinner.")
print(name.pop() + ", I'm very sorry to tell you that I can't invite you for dinner.")
print('I want to invite ' + name[0] + ' and ' + name[1] + ' for dinner.')
del name[0]
del name[0]
print(name)
