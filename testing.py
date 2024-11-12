test = []
answers = []



test = []
answers = []

with open("test.txt", "r") as file:
    for line in file:
        parts = line.strip().split("   ")
        if len(parts) == 2:
            test.append(parts[0])
            answers.append(parts[1])

print("Test:", test)
print("Answers:", answers)

