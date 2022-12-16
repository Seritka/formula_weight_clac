import periodictable as pt

formula = pt.formula(input('원하는 원소를 입력하세요: '))
print(f'분자량은 {formula.mass}/mol 입니다.')