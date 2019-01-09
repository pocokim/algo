def findDifference(str1, str2):
    str1List = list(str1)
    str2List = list(str2)
    str1List.sort()
    str2List.sort()

    str1List.append('~')

    for i in range(len(str2List)):
        if str2List[i] != str1List[i]:
            return str2List[i]


def main():
    print(findDifference("apple", "azlppe"))
    

if __name__ == "__main__":
    main()
