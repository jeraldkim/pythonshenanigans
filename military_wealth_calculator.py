raise_rate = 0.03 #연봉 인상률
investment_ROI = 0.08 #S&P500 평균 1년 수익
yearly_salary = 20137200 #2022하사 연봉 20137.2
salary_class_increase = 344400
saving_rate = 0.3
years_employed = 30
money_saved = 0

for i in range(1,years_employed):
    print(money_saved)
    money_saved *= (1 + investment_ROI)
    salary_saved = yearly_salary * saving_rate
    money_saved += salary_saved

    yearly_salary += salary_class_increase
    yearly_salary *= (1 + raise_rate)
    salary_class_increase *= (1 + raise_rate)

