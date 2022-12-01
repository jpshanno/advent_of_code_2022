import numpy as np

def read_data(fn):
  with open(fn) as f:
      calories = f.read().splitlines()
  return calories

def sum_calories_by_elf(dat):
  e = 0
  elves = [e]
  for c in dat:
    if c == '':
      e = e + 1
      elves.append(0)
      continue
    elves[e] = elves[e] + int(c)

  elves = np.asarray(elves)
  return elves

def get_max_cals(elves, n=1):
  return np.sum(-np.sort(-elves)[:n])

def answer(fn, n=1):
  dat = read_data(fn)
  elves = sum_calories_by_elf(dat)
  cals = get_max_cals(elves,n)
  if n == 1:
    answer = f'The elf with the most calories is carrying {cals} calories'
  else:
    answer = f'The {n} elves with the most calories are carrying {cals} calories'
  print(answer)

fn = "data/day_01.txt"
answer(fn, 1)
answer(fn, 3)