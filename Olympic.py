# 올림픽에 참가한 나라들의 순위를 결정하는 알고리즘
# 금, 은, 동메달 수가 주어지면 다음의 규칙에 따라 순위를 결정
# 1. 금메달 수가 더 많은 나라
# 2. 금메달 수가 같으면 은메달 수가 더 많은 나라. 금, 은메달 수가 닽으면 동메달 수가 더 많은 나라
# 각 국가는 1부터 N 사이의 정수로 표현. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1 로 정의
# 두 나라가 금, 은, 동메달 수가 모두 같으면 두 나라의 등수는 같음
# 각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램
# 입력 - 첫 줄은 국가의 수 N과 등수를 알고 싶은 국가 K가 빈칸을 사이에 두고 주어짐
# 이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수와 이 국가가 얻은 메달의 수가 빈칸을 사이에 두고 주어짐

# 메달 순으로 각 국가들을 비교하여 정렬하는 함수
def Ranking(countrys):
    # 금, 은, 동 메달 수를 기준으로 내림차순 정렬
    # x[1], x[2], x[3]는 튜플의 두 번째, 세 번째, 네 번째 항목을 의미
    # -x[1], -x[2], -x[3]: 마이너스 기호가 붙었으므로 내림차순으로 정렬합니다. 
    # 즉, x[1] 값이 클수록 먼저 오고, 그 다음으로 x[2]와 x[3]이 차례로 내림차순 정렬
    return sorted(countrys, key=lambda x: (-x[1], -x[2], -x[3]))

# 1. 입력 받는 첫 줄 - 국가의 수 N, 등수를 알고 싶은 국가 K
N, K = map(int, input().split())

# 국가별 정보를 저장할 리스트
countrys = []

# 2. 각 국가의 메달 수를 입력받음
for _ in range(N):
    # 국가 번호, 금메달, 은메달, 동메달 입력
    c, g, s, b = map(int, input().split())
    countrys.append([c, g, s, b])

# 3. 나라 별로 순위 매김
countrys = Ranking(countrys)

# 4. 동일한 순위를 처리하며 순위 매기기
rank = 1  # 첫 번째 순위는 1
ranks = [0] * N  # 각 국가의 순위를 저장할 리스트 (국가 번호에 맞춰 저장)

for i in range(len(countrys)):

    # 첫 번째 국가가 아니면서, 이전 국가와 메달 수가 같으면 같은 순위를 부여
    if i > 0 and countrys[i][1:] == countrys[i - 1][1:]:
        # 이전 국가와 메달 수가 같으면 같은 순위
        ranks[i] = ranks[i - 1]

    else:
        # 그렇지 않으면 새로운 순위 부여
        ranks[i] = rank

    rank += 1  # 다음 순위로 증가

# 5. K에 해당하는 국가의 순위를 출력
for i in range(len(countrys)):
    if countrys[i][0] == K:  # 국가 번호가 K와 같으면
        print(ranks[i])  # 그 국가의 순위를 출력
        break