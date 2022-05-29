import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from api.config import SPREADSHEET_ID

# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = SPREADSHEET_ID

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Пример чтения файла
def read_sheets(num_start: int,num_end: int):
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"A{num_start}:D{num_end}",
        majorDimension='ROWS'
    ).execute()
    #Проверяет полученный ответ от google, если нужного ключа нету
    #отправляет None
    return values.get('values')
