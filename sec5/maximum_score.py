scores = [130, 111, 90, 154, 194, 101, 100, 78, 54, 133, 88, 62, 123, 99, 70]

counter = scores[0]
for score in scores:
    if score > counter:
        counter = score

print(f"The maximum score is {counter}")

# The shortcut way is using max() in built function