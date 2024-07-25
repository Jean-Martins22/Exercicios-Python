#Balão++

import math

TORTA = 3.1415

def main():
    volume, raio = 0, 0
    qts_baloes, qts_gas = 0, 0

    raio, qts_gas = map(int, input().split())
    raio = raio ** 3

    volume = (4.0 * (TORTA * raio)) / 3.0

    while qts_gas > 0:
        qts_gas -= volume
        qts_baloes += 1

    print(qts_baloes - 1)

if __name__ == "__main__":
    main()
