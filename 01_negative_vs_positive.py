def result(pos, neg):
    pos_result = sum(pos) if pos else 0
    neg_result = sum(neg) if neg else 0
    print(neg_result)
    print(pos_result)
    if abs(neg_result) > pos_result:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


sequence_num = [int(x) for x in input().split()]
negatives = []
positives = []

num_type = [positives.append(sequence_num[i]) if sequence_num[i] > 0 else negatives.append(sequence_num[i]) for i in range(len(sequence_num))]
result(positives, negatives)