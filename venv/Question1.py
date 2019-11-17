import random

results = {
    'h': 0,
    't': 0,
}
sides = list(results.keys())
n = int(input())
for i in range(n):
    results[random.choice(sides)] += 1

print('Heads:', results['h'])
print('Tails:', results['t'])
