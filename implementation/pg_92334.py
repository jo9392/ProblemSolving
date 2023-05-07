from collections import defaultdict


def solution(id_list, report, k):
    reporter_dict = defaultdict(list)  # 유저별 유저가 신고한 사람
    reported_dict = defaultdict(int)  # 유저별 신고당한 횟수
    report_set = list(set(report))

    for re in report_set:
        reporter, reported = re.split()
        reporter_dict[reporter].append(reported)
        reported_dict[reported] += 1

    answer = [0] * len(id_list)
    for i in range(len(id_list)):
        for reported in reporter_dict[id_list[i]]:
            if reported_dict[reported] >= k:
                answer[i] += 1

    return answer