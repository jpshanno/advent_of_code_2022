fn = 'data/day_02.txt'
with open(fn) as f:
  dat = f.read().splitlines()

dat = [x.split(',') for x in dat]

def get_score(l):
  elf = ['A','B','C']
  throws = ['X','Y','Z']
  # Points for elf throw
  elf_value = 1 + elf.index(l[0])
  # Points for my throw
  throw_value = 1 + throws.index(l[1])
  score = throw_value
  # Tie
  if elf_value == throw_value:
    score = score + 3
  # Rock beats scissor
  elif (l[0] == 'A') & (l[1] == 'Z'):
    score = score + 0
  # Scissor loses to rock
  elif (l[0] == 'C') & (l[1] == 'X'):
    score = score + 6
  # Other cases of loss
  elif elf_value > throw_value:
    score = score + 0
  # Other cases of wins
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
  # If lose then get throw 1 worse than elf throw
  if outcome == 'X':
    throw = elf[elf_idx - 1]
  # If tie then get elf throw
  elif outcome == 'Y':
    throw = elf[elf_idx]
  # Else get throw 1 better than elf throw
  else:
    throw = elf[(elf_idx + 1) % 3]
  # Get value of throw
  throw_value = 1 + elf.index(throw)
  # Get total score
  score = score + 3 * outcomes.index(outcome) + throw_value
  
  return(score)

sum([get_new_score(x) for x in dat])