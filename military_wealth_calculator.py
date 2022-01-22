raise_rate = 0.04 #연봉 인상률 2006~2022 에서부터 딴 평균
investment_ROI = 0.08 #S&P500 평균 1년 수익

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

saving_rate = 0.3
years_employed = 30
money_saved = 0 #always 0 for initial start

for i in range(1,years_employed):
    print(money_saved)
    money_saved *= (1 + investment_ROI)
    salary_saved = yearly_salary * saving_rate
    money_saved += salary_saved

    yearly_salary += salary_class_increase
    yearly_salary *= (1 + raise_rate)
    salary_class_increase *= (1 + raise_rate)

def