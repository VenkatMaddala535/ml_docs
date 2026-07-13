import math

def gini(labels):
    total = len(labels)

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    impurity = 1

    for count in counts.values():
        p = count / total
        impurity -= p ** 2

    return impurity


def entropy(labels):
    total = len(labels)

    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1

    ent = 0

    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)

    return ent


# Pure node
data1 = ["Yes", "Yes", "Yes", "Yes"]

print("Pure Node")
print("Gini   :", gini(data1))
print("Entropy:", entropy(data1))

# Mixed node
data2 = ["Yes", "Yes", "No", "No"]

print("\nMixed Node")
print("Gini   :", gini(data2))
print("Entropy:", entropy(data2))


data3 = ["Yes", "No", "No", "No"]

print("\nMixed Node")
print("Gini   :", gini(data2))
print("Entropy:", entropy(data2))
