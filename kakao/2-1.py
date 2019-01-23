
def dartResult(str1):
    scores= []
    count = 0
    for i in range(len(str1)):
        try:
            nowScore = int(str1[i])
            count += 1
            if (nowScore == 0) and (str1[i-1] == '1'):
                nowScore = 10
                count -= 1
        except:
            if str1[i] == 'S':
                scores.append(nowScore)
            elif str1[i] == 'D':
                scores.append(nowScore**2)
            elif str1[i] == 'T':
                scores.append(nowScore**3)
            elif str1[i] == '*':
                if count == 1:
                    scores[0] *= 2
                elif count == 2:
                    scores[0] *= 2
                    scores[1] *= 2
                elif count == 3:
                    scores[1] *= 2
                    scores[2] *= 2
            elif str1[i] == '#':
                scores[-1] *= -1
    return sum(scores)
