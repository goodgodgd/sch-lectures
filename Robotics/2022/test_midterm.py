from midterm_correct_answer import *

print("=== 1. index word")
text = "pick me pick me pick me up"
word = "pick"
result = index_word(text, word)
print(f"result={result}\n")

print("=== 2. sum list")
data = [1, 2, 3, 10, 4, 5]
result = sum_list(data)
print(f"result1={result}")
result = sum_list(data, 10)
print(f"result2={result}\n")

print("=== 3. add dicts")
foo = {'kim': 1, 'lee': 2}
bar = {'lee': 3, 'park': 4}
result = add_dicts(foo, bar)
print(f"result1={result}")
result = add_dicts(foo, bar, True)
print(f"result2={result}\n")

print("=== 4. manipulate_list")
tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
result = manipulate_list(tottenham, sort_first=True,
                         remove=["Ali", "Eriksen", "Llorente"],
                         append=["Kulusevski", "Bentancur", "Romero"])
print(f"result1={result}")
tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
result = manipulate_list(tottenham, pop=[2],
                         remove=["Eriksen", "Llorente"],
                         append=["Kulusevski", "Bentancur", "Romero"],
                         sort_last=True)
print(f"result2={result}")
tottenham = ["Son", "Kane", "Ali", "Eriksen", "Llorente"]
result = manipulate_list(tottenham, pop=[2, 4, 3],
                         append=["Kulusevski", "Bentancur", "Romero"],
                         sort_last=True)
print(f"result3={result}\n")

print("=== 5. Statistics")
stat = Statistics([1, 2, 3, 4, 5])
print("mean=", stat.mean())
print("max=", stat.max())
print("max_with=", stat.max_with([5, 4, 3, 2, 1]))


