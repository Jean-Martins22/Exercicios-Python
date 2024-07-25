#Ih, Ferrou, um Buraco Negro!

def encontrar_centro(x0, y0, x1, y1):
    return (x0 + x1) / 2, (y0 + y1) / 2

def coeficiente_angular(x0, y0, x1, y1):
    if x1 == x0:
        return None
    return (y1 - y0) / (x1 - x0)

def intersecao(m1, b1, m2, b2):
    if m1 is None:
        x = b1
        y = m2 * x + b2
    elif m2 is None:
        x = b2
        y = m1 * x + b1
    else:
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
    return x, y

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for i in range(1, T + 1):
        x1_0 = float(data[index])
        y1_0 = float(data[index + 1])
        x2_0 = float(data[index + 2])
        y2_0 = float(data[index + 3])
        x1_1 = float(data[index + 4])
        y1_1 = float(data[index + 5])
        x2_1 = float(data[index + 6])
        y2_1 = float(data[index + 7])
        index += 8
        
        C1_x, C1_y = encontrar_centro(x1_0, y1_0, x1_1, y1_1)
        C2_x, C2_y = encontrar_centro(x2_0, y2_0, x2_1, y2_1)
        
        m1 = coeficiente_angular(x1_0, y1_0, x1_1, y1_1)
        m2 = coeficiente_angular(x2_0, y2_0, x2_1, y2_1)
        
        if m1 is not None:
            if m1 != 0:
                m1_perpendicular = -1 / m1
            else:
                m1_perpendicular = float('inf')
            b1 = C1_y - m1_perpendicular * C1_x
        else:
            m1_perpendicular = 0  # Linha vertical
            b1 = C1_y
        
        if m2 is not None:
            if m2 != 0:
                m2_perpendicular = -1 / m2
            else:
                m2_perpendicular = float('inf')
            b2 = C2_y - m2_perpendicular * C2_x
        else:
            m2_perpendicular = 0
            b2 = C2_y
        
        X, Y = intersecao(m1_perpendicular, b1, m2_perpendicular, b2)
        
        results.append("Caso #{}: {:.2f} {:.2f}".format(i, X, Y))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
