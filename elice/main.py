class Solution:
    def solution(self,masks):
        a= len(masks[0]) # masks 배열 원소의 길이
        temp =[]
        count2 = 0

        if len(masks) <=2 :
            return 'NO'

        for i in range(a):
            for j in range(len(masks)):
                temp.append(masks[j][i])        
            
            count = 0
            for k in range(len(temp)):
                if temp[k] == '1':
                    count +=1

            
            if count >=2 and temp.index('0') != None :
                count2 += 1
            else:
                return 'NO'
            temp = []
            
        # print(count2)

        if count2 == a:
            return 'YES'
            
            

        # for i in range(len(masks)):
        #     print(masks[i])



            # for i in range(len(mask)):
            #     print(mask[i],end=" ")
            # print('')
            #     print(masks[i][j])
            # print(masks[i])

        # if masks
        

masks = ["010","011","000"]
# masks = ["1","0","1","0"]
# masks = ["11111"]
# masks = ["0110011","0101001","1111010","1010010"]
# masks =["101001011","011011010","010110010","111010100","111111111"]



print(Solution().solution(masks))



