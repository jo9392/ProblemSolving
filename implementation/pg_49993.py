import re


def solution(skill, skill_trees):
    skill_list = list(skill)
    for j in range(len(skill_trees)):
        for i in range(len(skill_list)):
            skill_trees[j] = skill_trees[j].replace(skill_list[i], str(i))
        skill_trees[j] = re.sub(r"[^0-9]", "", skill_trees[j])

    answer = len(skill_trees)
    for skill_str in skill_trees:
        if len(skill_str) == 0:
            continue
        elif len(skill_str) - 1 != int(max(skill_str)):
            answer -= 1
            continue
        for i in range(1, len(skill_str)):
            if skill_str[i - 1] > skill_str[i]:
                answer -= 1
                break

    return answer