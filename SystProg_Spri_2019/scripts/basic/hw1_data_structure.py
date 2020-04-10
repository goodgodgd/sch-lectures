heroes = ["iron man", "thor", "spider man", "hulk", "captain america", "hawkeye"]
print("original heroes:", heroes)
# 1. 히어로들을 알파벳 역순으로 정렬하시오.
heroes.sort(reverse=True)
print("1. sorted heroes:", heroes)

# 2. 아래 new_heroes에서 첫번째와 마지막 히어로를 제거하고 captain marvel과 hawkeye을 추가하시오.
new_heroes = [hero for hero in heroes]
new_heroes.pop(0)
del new_heroes[-1]
new_heroes.append("captain marvel")
new_heroes.append("spider man")
print("2. change heroes:", new_heroes)

# 3. for문을 이용하여 'man'으로 끝나는 히어로 이름에서 'man'을 'woman'으로 바꾼 새 리스트 heroines를 만드시오.
heroines = []
for hero in heroes:
    if "man" in hero:
        heroines.append(hero.replace("man", "woman"))
print("3. transgender heroines:", heroines)

# 4. list comprehension을 이용하여 'woman'이 들어간 히어로 이름을 'human'으로 바꾼 새 리스트 neutralized_heroes를 만드시오.
neutralized_heroes = [hero.replace("woman", "human") for hero in heroines]
print("4. neutralized heroes:", neutralized_heroes)

# 5. 2의 heroes에서 enumerate를 이용하여 홀수번째 히어로만 뽑아낸 새 리스트 odd_heroes를 만드시오.
odd_heroes = []
for i, hero in enumerate(heroes):
    if i%2 == 1:
        odd_heroes.append(hero)
print("5.1 odd heroes", odd_heroes)
odd_heroes = [hero for i, hero in enumerate(heroes) if i%2==1]
print("5.2 odd heroes", odd_heroes)

# 6. for문에 zip 함수를 써서 5의 히어로 이름과 배우 이름을 딕셔너리로 묶은 hero_actors를 만들어 보시오.
actor_names = ["햄식이", "톰 홀랜드", "로다주", "마크 러펄로"]
hero_actors = {hero: name for hero, name in zip(heroes, actor_names)}
print("6. hero actors", hero_actors)
print("6. thor was played by", hero_actors["thor"])
print("6. spider man was played by", hero_actors["spider man"])

# 7. 2의 new_heroes를 연기한 배우들의 이름을 6의 hero_actors를 이용해 출력하시오.
# 이름이 있으면 6번과 같이 이름을 출력하고 없으면 "?? has no name"을 출력하시오.
for hero in new_heroes:
    if hero in hero_actors:
        print(f"7. {hero} was played by {hero_actors[hero]}")
    else:
        print(f"7. {hero} has no name")
