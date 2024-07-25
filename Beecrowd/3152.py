#Samuel, O Cafeicultor

def calculate_area(vertices):
    x1, y1 = vertices[0]
    x2, y2 = vertices[1]
    x3, y3 = vertices[2]
    x4, y4 = vertices[3]
    
    area = 0.5 * abs(x1*y2 + x2*y3 + x3*y4 + x4*y1 - (y1*x2 + y2*x3 + y3*x4 + y4*x1))
    return area

def main():
    vertices_A = []
    vertices_B = []
    
    for _ in range(4):
        x, y = map(int, input().split())
        vertices_A.append((x, y))
    
    for _ in range(4):
        x, y = map(int, input().split())
        vertices_B.append((x, y))
    
    area_A = calculate_area(vertices_A)
    area_B = calculate_area(vertices_B)
    
    if area_B >= area_A:
        print("terreno B")
    else:
        print("terreno A")

if __name__ == "__main__":
    main()
    