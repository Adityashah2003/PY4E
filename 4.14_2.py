def computegrade (a):
    score = int(a)
    if score >= 0.9:
        return("A")
    elif score >= 0.8:
        return("B")
    elif score >= 0.7:
        return("C")
    elif score < 0.6:
        return("F")

input_score = input('Enter score: ')
score = float(input_score)
grade = computegrade (score)
print(grade)

