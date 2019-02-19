class Solution:
    def solution(self, masks):
        n = len(masks) # 비트마스크판의 갯수 
        m = len(masks[0]) # 비트마스크판의 길이
        
        if n < 3:
            return 'NO'
        
        for j in range(m): # 두번쨰로 반복될게 바깥으로 간다. 
            temp =[]
            for i in range(n): # 첫번째로 반복될게 안으로 들어가고
                temp.append(masks[i][j])
                   
        # mask[0][0] , mask[1][0] , mask[2][0] 의 비교
        # 2차원 배열 데이터 뽑아내는것의 어려움. 
        # i랑 j는 단순한 변수일뿐이고, 첫번째로 반복될것과 두번째로 반복될것이 핵심이다.
        # 헷갈린다면 첫번째로 반복될것을 i로 선언하는것이 차라리 좋을듯.
            
            
            # print(temp)
            if '0' not in temp: # 0포함여부 확인
                return 'NO'
            if temp.count('1') <2: # '1'의 갯수 확인 
                return 'NO'
        
            temp =[]
            
            
        return 'YES' #  두번째 반복문까지 모두 통과한 다음에야 yes를 리턴 
        
        # 키포인트
        # 2차원 배열 데이터 뽑아내기
        # '1'과 1, 문자와 숫자 항상 구분잘하기
        # 반복문과 return 위치 제대로 확인하기


