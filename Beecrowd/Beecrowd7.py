def remove_candidates(N, k, m):
    candidates = list(range(1, N + 1))
    removed = []

    i = 0  # índice para o contador no sentido horário
    j = N - 1  # índice para o contador no sentido anti-horário

    while candidates:
        i = (i + k - 1) % len(candidates)
        j = (j - m) % len(candidates)

        if i == j:
            removed.append(candidates.pop(i))
        else:
            removed.append(candidates.pop(i))
            if j < i:
                j = (j + 1) % len(candidates)  # ajuste para garantir que j permaneça dentro dos limites
            removed.append(candidates.pop(j))

        if not candidates:
            break

    return removed


while True:
    try:
        N, k, m = map(int, input().split())
        if N == 0 and k == 0 and m == 0:
            break

        removed_candidates = remove_candidates(N, k, m)
        output = ", ".join("?" if x == -1 else str(x) for x in removed_candidates)
        print(output)
    except ValueError:
        print("Por favor, insira apenas números inteiros.")
