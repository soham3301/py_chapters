scores = [130, 111, 90, 154, 194, 101, 100, 78, 54, 133, 88, 62, 123, 99, 70]

total_score = sum(scores)
print(total_score)

# Using for loops instead of sum()

total_sum = 0
for score in scores:
    total_sum = total_sum + score

print(total_sum)

# Figuring out maximum number using max()
maximum_score = max(scores)
print(maximum_score)

