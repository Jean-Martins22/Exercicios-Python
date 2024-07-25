#Babel

from collections import defaultdict
from heapq import heappop, heappush

def solve():
    M = int(input())
    if M == 0:
        return False

    O, D = input().split()
    words = defaultdict(list)
    for _ in range(M):
        I1, I2, P = input().split()
        words[I1].append((I2, P))
        words[I2].append((I1, P))

    dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
    dist[O][''] = 0
    queue = [(0, O, '')]
    while queue:
        d, lang, last_word = heappop(queue)
        if lang == D:
            return d
        if d != dist[lang][last_word]:
            continue
        for next_lang, word in words[lang]:
            if last_word and last_word[0] == word[0]:
                continue
            if d + len(word) < dist[next_lang][word]:
                dist[next_lang][word] = d + len(word)
                heappush(queue, (d + len(word), next_lang, word))
    return 'impossivel'

while True:
    result = solve()
    if result is False:
        break
    print(result)
