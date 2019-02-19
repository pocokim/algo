def solution(board, nums):
    n = len(board)
    vertical = [0 for _ in range(n)]
    horizontal = [0 for _ in range(n)]
    lu_diag = 0
    ru_diag = 0

    # 탐색을 O(1)로 하기 위해 nums를 set 자료구조로 변환
    # 들어오는 순서가 상관없기때문에 set으로 받아서 처리
    
    nums = set(nums)

    for p in range(n):
        for q in range(n):
            if board[p][q] in nums: # board에 nums가 어디있는지가 아니라 nums에 board[p][q]값이 있는지로 찾았음. 이게 오히려 인덱스 알기가 편해서 좋은듯 
                horizontal[q]+=1
                vertical[p]+=1

                if p == q:
                    lu_diag+=1
                if p + q == n - 1:
                    ru_diag += 1

    cnt = 0

    # 가로와 세로를 어떻게 처리할까 고민했는데 가로배열, 새로배열을 만들어서 계산할 생각은 못함.
    # 그냥 단순히 있으면 0으로 변경하고 가로,세로가 0000 과 같은 형태인지 확인해주려고 했었음. 

    cnt += vertical.count(n)
    cnt += horizontal.count(n)
    if lu_diag == n:
        cnt += 1
    if ru_diag == n:
        cnt += 1
    return cnt

print(solution([[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]],[11,13,15,16,1,4,3,2,5,14]))