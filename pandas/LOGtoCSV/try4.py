def list_split(listA, n):
    for x in range(0, len(listA), n):
        every_chunk = listA[x: n+x]

        if len(every_chunk) < n:
            every_chunk = every_chunk + \
                [None for y in range(n-len(every_chunk))]
        yield every_chunk
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
list1=['$', '1', 'SECURE', 'SAM1.0', 'DT', 'L', '864337052899292', 'TN04E1234', '0', '06012080', '002633', '00.000000', '0', '00.0000000', '0', '000.00', '000', '00', '0000', '00.0', '00.0', 'BSNL', '1', '1', '15.0', '0.0', '0', 'W', '00', '000', '000', '00000', '00000', '0', '0000', '00', '000158', '107', '*', '$', '1', 'SECURE', 'SAM1.0', 'DT', 'L', '864337052899292', 'TN04E1234', '0', '06012080', '002643', '00.000000', '0', '00.0000000', '0', '000.00', '000', '00', '0000', '00.0', '00.0', 'BSNL', '1', '1', '15.0', '0.0', '0', 'W', '00', '000', '000', '00000', '00000', '0', '0000', '00', '000159', '109', '*']
print(len(list1))
listA,listB=split_list(list1)
print(listA)
print("\n",listB)
