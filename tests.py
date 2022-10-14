import pytest

from main import CashCalculator, CaloriesCalculator, Record, calories_calculator


@pytest.fixture()
def cash_calc():
    cash_calculator = CashCalculator(1300)
    cash_calculator.add_record(Record(amount=1186, comment='Кусок тортика. И ещё один.'))
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
    cash_calculator.add_record(Record(amount=145, comment='Безудержный шопинг', date='08.03.2019'))
    cash_calculator.add_record(Record(amount=1568, comment='Наполнение потребительской корзины', date='09.03.2019'))
    cash_calculator.add_record(Record(amount=6917, comment='Катание на такси', date='08.03.2019'))
    return cash_calculator


@pytest.fixture()
def cal_calc():
    calories_calculator = CaloriesCalculator(1000)
    calories_calculator.add_record(Record(amount=1186, comment='Кусок тортика. И ещё один.', date='24.02.2019'))
    calories_calculator.add_record(Record(amount=145, comment='кофе'))
    calories_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    calories_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
    return calories_calculator

def test_cashCalc(cash_calc):
    assert cash_calc.get_today_cash_remained('RUB') == 'No money, but you hold on. Your duty:  3331.0 rub'

def test_CalCalc(cal_calc):
    assert cal_calc.get_calories_remained() == 'Stop eating'

def test_cal_Limit(cal_calc):
    assert cal_calc.remained() < 1000

def test_cashCalc_limit(cash_calc):
    assert cash_calc.get_today_start() > 0