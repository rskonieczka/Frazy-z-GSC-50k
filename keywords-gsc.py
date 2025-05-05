from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import pandas as pd
import datetime

scopes = ['https://www.googleapis.com/auth/webmasters.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name('indexing-api.json', scopes)
service = build('webmasters', 'v3', credentials=credentials)

# Automatyczne wyliczanie zakresu dat: od dziś do 16 miesięcy wstecz
today = datetime.date.today()
sixteen_months_ago = today - datetime.timedelta(days=16*30)  # uproszczone 16 miesięcy (480 dni)

start_date = sixteen_months_ago.strftime('%Y-%m-%d')
end_date = today.strftime('%Y-%m-%d')

all_rows = []
start_row = 0
row_limit = 25000

while True:
    request = {
        'startDate': start_date,
        'endDate': end_date,
        'dimensions': ['query'],
        'rowLimit': row_limit,
        'startRow': start_row
    }
    response = service.searchanalytics().query(
        siteUrl='https://TwojaDomena.pl/',
        body=request
    ).execute()
    rows = response.get('rows', [])
    if not rows:
        break
    all_rows.extend(rows)
    if len(rows) < row_limit:
        break
    start_row += row_limit

# Konwersja do DataFrame
if all_rows:
    df = pd.DataFrame(all_rows)
    df.to_csv(f'frazy_gsc_{start_date}_{end_date}.csv', index=False)
else:
    print('Brak danych do zapisania w podanym zakresie dat.')
