LINK_TO_LOGIN_PAGE = r'private'
LINK_TO_MAIN_PAGE = r'private'
CHROME_DRIVER_PATH = r'chromedriver.exe'
EXCEL_ROW_OFFSET = 0 #How many first patients in the table are skipped
NAME_OF_DOC_SERIES_HEADER = 'Документ серия'
NAME_OF_DOC_NUMBER_HEADER = 'Документ номер'

import configparser
conf = configparser.ConfigParser()
conf.read('config.ini')
row_indices = {}
for item in conf['DEFAULT']:
    row_indices[item.upper()] = int(conf['DEFAULT'][item])
print(row_indices)
SURNAME_ROW = 0
NAME_ROW = 1
PATRONYMIC_ROW = 2
GENDER_ROW = 3
BIRTH_DATE_ROW = 4
PHONE_NUMBER_ROW = 5
DOCUMENT_TYPE_ROW = 6
DOCUMENT_SERIES_ROW = 7
DOCUMENT_NUMBER_ROW = 8
WHO_GAVE_DOCUMENT_ROW = 9
DATE_DOCUMENT_GIVEN_ROW = 10
SAMPLE_TAKEN_DATE_ROW = 12
SAMPLE_TAKEN_TIME_ROW = 13
REG_ADDRESS_ROW = 14
LIVING_ADDRESS_ROW = 15
WORKPLACE_NAME_ROW = 16
WORKPLACE_ADDRESS_ROW = 17
RESULT_DATE_ROW = 18
RESULT_TIME_ROW = 19
IDS_ROW = 20
SNILS_ROW = 21
