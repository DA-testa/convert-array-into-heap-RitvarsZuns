# python3


def build_heap(data):
    swaps = []
    n = len(data)
    for i in range(n // 2, -1, -1):
        j = i
        while True:
            left = j * 2 + 1
            right = j * 2 + 2
            smallest = j
            if left < n and data[left] < data[smallest]:
                smallest = left
            if right < n and data[right] < data[smallest]:
                smallest = right
            if smallest != j:
                swaps.append((j, smallest))
                data[j], data[smallest] = data[smallest], data[j]
                j = smallest
            else:
                break
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    mode = input()
    if "I" in mode:
        n = int(input())
        data = list(map(int, input().split()))
    elif "F" in mode:
        filename = input()
        if 'a' in filename:
            return
        with open(f"tests/{filename}") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))


    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
