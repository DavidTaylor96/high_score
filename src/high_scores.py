def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    if scores == scores:
        return "There is a tie!"
    else:
        return sorted(scores, reverse=True)[:3]

def highest_to_lowest(scores):
    return sorted(scores, reverse=True)

def tie_top_three(scores):
    new_list = []
    new_list.append(personal_top_three)
    return ["There is a Tie!" for number in new_list if number == number ]