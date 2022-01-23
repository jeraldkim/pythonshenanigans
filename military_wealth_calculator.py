raise_rate = 0.04 #연봉 인상률 2006~2022 에서부터 딴 평균
investment_ROI = 0.08 #S&P500 평균 1년 수익
monthly_ROI = (1 + investment_ROI)**(1/12) - 1
#0.00643
current_year = 0

v1_monthly_salary = 1705400 #하사 2022 월급
v2_monthly_salary = 1791100
v3_monthly_salary = 2220700
v4_monthly_salary = 3210800
d1_monthly_salary = 2289600

v1_salary_class = 29200 #하사 호봉으로 인한 월급 증가
v2_salary_class = 92100
v3_salary_class = 98500
v4_salary_class = 102600
d1_salary_class = 108900

saving_rate = 0.2
years_employed = 30
money_saved = 0 #always 0 for initial start


def v1_class(year): #하사 호봉 계산기
    return year + 1

def v2_class(year):
    if year < 3:
        return 1
    else:
        return year - 1

def v3_class(year):
    if year < 6:
        return 1
    else:
        return year - 4

def v4_class(year):
    if year < 14:
        return 1
    else:
        return year - 12

def d1_class(year):
    return v1_class(year)

def rank_salary(year, rank):
    if rank == 1:
        return v1_monthly_salary + v1_salary_class * v1_class(year)
    elif rank == 2:
        return v2_monthly_salary + v2_salary_class * v2_class(year)
    elif rank == 3:
        return v3_monthly_salary + v3_salary_class * v3_class(year)
    elif rank == 4:
        return v4_monthly_salary + v4_salary_class * v4_class(year)
    elif rank == 5:
        return d1_monthly_salary + d1_salary_class * d1_class(year)
    else:
        return 0

def salary(year, rank):
    return rank_salary(year, rank)*(1+raise_rate)**year

def rank_calculator(year): #상사 까지만 진급한다는 가정
    if year < 5:
        return 1
    elif year < 10:
        return 2
    else:
        return 3

#monthly_ROI = 0 
for years in range(1,years_employed+1):
    current_rank = rank_calculator(current_year)
    for months in range(12):
        money_saved = money_saved * (1 + monthly_ROI)
        salary_saved = salary(current_year,current_rank) * saving_rate
        money_saved += salary_saved
    current_year += 1
    print(money_saved)
    