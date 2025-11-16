
# Using pass With Conditional Statement

n = 10

# use pass inside if statement
if n > 10:
    pass # is used to move forward instead of writing code and left this step for future purposes

print('Hello')

# next run
print(" Next Run...")

#Example: break Statement with for Loop
for i in range(5):
    if i == 3:
        break # means stop peocessing here, stop present loop or further also 
    print(i)

# next run
print(" Next Run...")

#Example: continue Statement with for Loop

for i in range(5):
    if i == 3:
        continue # is used to stop present but doesnot stop further executions
    print(i)


# next run
print(" Next Run...")

i = 0

while i < 5:
    if i == 3:
        break
    print(i)
    i += 1