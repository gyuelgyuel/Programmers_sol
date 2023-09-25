def solution(n):
    prime_list = [] # 소수 저장 배열
    i=2
    while i<=n:  # 2부터 n까지
        is_prime = True
        div_max = int(n**0.5)
        for j in prime_list:    # i전의 소수들로 나눠보고 나눠지면 소수 아님
            if j>div_max:       # 루트값보다 낮은 경우만 나눠보기
                break
            if i%j==0:
                is_prime=False
                break
        if is_prime:            # 소수면 배열에 추가
            prime_list.append(i)
        i+=1
    return len(prime_list)