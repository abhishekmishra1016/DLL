bias = []
weight = []
threshold = int(input("Enter Threshold: "))
res = 0

n = int(input("How many values to be inserted? "))
while n>0:
    x = int(input("Insert Weight: "))
    weight.append(x)
    y = int(input("Insert Bias: "))
    bias.append(y)
    for i in range(len(weight)):
        res = res + weight[i] + bias[i]
        if res>=threshold:
            print("---->Neuron will fire")
        else:
            print("---->Neuron won't fire")
    n = n-1          

print("Bias:", bias)
print("Weights: ", weight)