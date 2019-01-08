import copy
testcase = int(input())
for i in range(1,testcase+1):

    total , colors = input().split()
    prisoner_cars = list(map(int,input().split())) # 차의 색깔별 수
    gate = list(map(int,input().split())) # 게이트에 들어온 차의 종류 
    printer = list()

    count2 = 0
    for l in range(len(prisoner_cars)):
        count2 += prisoner_cars[l]
    print(count2)    

    arc = copy.deepcopy(prisoner_cars)
    print(arc)


    want = '1'*count2
    print(want)
    print('색깔의 갯수와 찾고자하는 연속된1의 형태출력')

    # 반복문의 i나 j값을 연결되도록 변경시켜주어야함.
    def make_new_gate(j):
        arc = copy.deepcopy(prisoner_cars)
        # print(arc)
        
        for i in range(j,len(gate)):
            

            if prisoner_cars[gate[i]-1] != 0 and arc[gate[i]-1] > 0 :
                new_gate[i] = 1
                arc[gate[i]-1] -= 1
                print('실행중')
                print(arc)
                if sum(arc) == 0:               
                    break;

            else :
                    new_gate[i] = 0
            print('new게이트의 변화찾기')
            print(str(i+1)+"번째반복문 실행")
            print(new_gate)

        print('for문이 끝난뒤의 '+str(j)+"번째게이트")            
        print(new_gate)
        return new_gate






    # 색깔별 차 확인 

    for j in range(len(gate)):
        new_gate = ["0" for i in range(len(gate))]
        # print(new_gate)
        make_new_gate(j)
            

        # print(str(j)+"번째게이트")
        # print(new_gate)

        gate_string=""
        for k in range(len(gate)):
            gate_string += str(new_gate[k])

        #list형태의 new gate를 string으로 바꿔줌
        # print(gate_string)

    
        printer.append(int(gate_string.find(want))+1)
        # print('printer 리스트 출력')
        # print(printer)


    # print('반복문이 모두 끝난뒤의 printer리스트 츌력')
    # print(printer)

    # for i in range(len(printer)):
    #     if printer[i] != 0:

    printer.sort()
    printer.reverse()
    a= printer.index(0)
    del printer[a:]

    print('소팅이 끝난다음의 프린터 출력 ')
    print(printer)
        
    print('원하는 인덱스 출력')    
    if len(printer) != 0 :
        print('#'+str(i)+' '+str(min(printer)))
    else :
        print('#'+str(i)+' '+str(int(0)))


    # for i in range(real_length):
    #     if printer[i] == 0 : 
    #         del printer[i]


        # gate_string = ''.join(str(gate))
        # print(gate_string)

        # print(prisoner_cars)
        



    # 배령릐 오른쪽 값도 1인지 확인하고 , 

            
            