def solution(rank, attendance):
                                                         # rank.index(x) : x등수 학생의 학생번호(index) 반환
                                              # attendance : i번 학생의 참석 여부
                               # lambda 함수 : 참석하면 그대로 x, 불참이면 최대값보다 1 큰 101(꼴지) 반환
               # sorted, list, map : lambda함수에 따라 매핑후 리스트로 변환 후, 오름차순 정렬
    att_rank = sorted(list(map(lambda x: x if attendance[rank.index(x)] else 101, rank)))
                   # 1등의 학생번호                  # 2등의 학생번호            # 3등의 학생번호
    return 10000 * rank.index(att_rank[0]) + 100 * rank.index(att_rank[1]) + rank.index(att_rank[2])