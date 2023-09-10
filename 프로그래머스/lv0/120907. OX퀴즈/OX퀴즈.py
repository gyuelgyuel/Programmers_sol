def solution(quiz):
    answer = []
    for q in quiz:
        X, opr, Y, eql, Z = q.split(" ")
        num = []
        for n in [X,Y,Z]:
            sign = 1
            if n[0] == "-":
                sign = -1
                n = n[1:]
            num.append(sign * int(n))
        x, y, z = num
        if opr == "-":
            if x - y == z:
                answer.append("O")
            else:
                answer.append("X")
        elif opr == "+":
            if x + y == z:
                answer.append("O")
            else:
                answer.append("X")
        
    return answer