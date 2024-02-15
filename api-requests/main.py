import requests
import xlsxwriter


count = 51
# открываем новый файл на запись
workbook = xlsxwriter.Workbook('/Users/apnalimov/Documents/testApiNumbers.xlsx')
# создаем там "лист"
worksheet = workbook.add_worksheet()
for i in range(1, int(count)):
    url = f'http://numbersapi.com/{i}'
    # делаем гет запрос с аргументом url
    response = requests.get(url)
    # записываем данные в ячейку
    worksheet.write(f'A{i}', 'status code')
    worksheet.write(f'A{i}', f'{response.status_code}')
    worksheet.write(f'B{i}', 'response text')
    worksheet.write(f'B{i}', f'{response.text}')
    worksheet.write(f'C{i}', 'headers')
    worksheet.write(f'C{i}', f'{response.headers}')
    worksheet.write(f'D{i}', 'json')
    worksheet.write(f'D{i}', f'{response.json}')
    print(f'{i} --- Done.')
# сохраняем и закрываем
workbook.close()

print('End.')