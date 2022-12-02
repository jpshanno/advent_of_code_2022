fn = 'data/day_02.txt'
with open(fn) as f:
  dat = f.read().splitlines()

dat = [x.split(',') for x in dat]

def get_score(l):
  elf = ['A','B','C']
  throws = ['X','Y','Z']
  score = 0
  elf_value = 1 + elf.index(l[0])
  throw_value = 1 + throws.index(l[1])
  score = score + throw_value
  if elf_value == throw_value:
    score = score + 3
  elif (l[0] == 'A') & (l[1] == 'Z'):
    score = score + 0
  elif (l[0] == 'C') & (l[1] == 'X'):
    score = score + 6
  elif elf_value > throw_value:
    score = score + 0
  else:
    score = score + 6

  return(score)

scores = [get_score(x) for x in dat]
sum(scores)


def get_new_score(l):
  elf = ['A','B','C']
  outcomes = ['X','Y','Z']
  outcome = l[1]
  score = 0
  elf_idx = elf.index(l[0])
  if outcome == 'X':
    throw = elf[elf_idx - 1]
  elif outcome == 'Y':
    throw = elf[elf_idx]
  else:
    throw = elf[(elf_idx + 1) % 3]
  throw_value = 1 + elf.index(throw)
  score = score + 3 * outcomes.index(outcome) + throw_value
  
  return(score)

sum([get_new_score(x) for x in dat])