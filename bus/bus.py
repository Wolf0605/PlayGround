import random
import math
# 사람 수, 정류장 수, 하차태그를 안 찍는 비율
population = 50
station = 27
rate = float(10/100)

# 사람과 정류장을 숫자로 개별 인식
human = [i for i in range(population)]
station_number = [i for i in range(1, station+1)]


# 승차 하는 버스 정류장 번호 (맨 마지막 정류장에선 탈 수 없음)
ride_bus_station = [i for i in range(1, station)]
ride_station = random.choices(ride_bus_station, weights = None, k = population)
# print(ride_station)

# 하차 하는 버스 정류장 번호
drop_station = []
for bus in ride_station:
  one_person_drop = random.randint(bus+1, station)
  drop_station.append(one_person_drop)

# zip 함수로 승객, 승차홈, 하차홈 묶기
zip_lst = list(zip(human, ride_station, drop_station))
# 시각화
# print('승객        승차         하차')
# for i in range(population):
#     print(zip_lst[i][0],"         ",zip_lst[i][1],"         ",zip_lst[i][2])

# 블라인드 처리
drop_rate = round(population * rate)
blind = random.sample(human, k=drop_rate)
bld = []
bld += drop_station
for i in range(population):
    if zip_lst[i][0] in blind:
        bld[i] = 'X'
# 블라인드 시각화
print('승객        승차         하차')
for i in range(population):
    print(zip_lst[i][0],"         ",zip_lst[i][1],"         ",bld[i])

# 블라인드 인 사람들만 추려내고 정렬 해보기
blind_lst = []
for i in blind:
    blind_lst.append(zip_lst[i][0])
blind_lst.sort()

n = 1
r = 0
d = 0
percent = 1

# 버스는 계속 정거장을 지나가면서 나아간다
for n in range(1, station+1):
    # 버스는 지나가면서 정거장에 있는 사람들을 태운다
    for i in range(population):
        if zip_lst[i][0] in blind_lst:
            if zip_lst[i][1] == n:
                r += 1
        else:
            pass
    # 버스는 지나가면서 사람들을 내린다
    for i in range(population):
        if zip_lst[i][0] in blind_lst:
                if zip_lst[i][2] == n:
                    d += 1
    if d > 0:
        percent = percent * round((math.factorial(d) / ((math.factorial(r) / math.factorial(r-d)))),2)
    # 사람을 내려주는 수식
    while True:
        if d > 0:
            r -= 1
            d -= 1
        else:
            break
# X 들이 실제로 탄곳 내린곳 보여주기
print('블라인드 처리한 사람들')
print('승객        승차         하차')
for i in blind_lst:
    print(zip_lst[i][0],"         ",zip_lst[i][1],"         ",zip_lst[i][2])
# 점수 보여주기
print(percent * 100)