import datetime as dt
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    terms = list(t.split() for t in terms)
    privacies = list(p.split() for p in privacies)
    terms_dict = dict(terms)
    today = dt.datetime.strptime(today, "%Y.%m.%d")
    answer = []
    for i in range(len(privacies)):
        start_day = dt.datetime.strptime(privacies[i][0], "%Y.%m.%d")
        end_day = start_day +relativedelta(months=int(terms_dict[privacies[i][1]]))
        if end_day <= today:
            answer.append(i+1)

    return answer