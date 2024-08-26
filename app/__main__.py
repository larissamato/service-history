import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import requests
from app.models import SessionLocal, Report
from app.config import API_URL, HEADERS, INITIAL_DATE

def fetch_page(page):
    initial_date = INITIAL_DATE if INITIAL_DATE else datetime.now().strftime('%Y-%m-%d')
    params = {
        'data_inicial': initial_date,
        'data_final': datetime.now().strftime('%Y-%m-%d'),
        'id_conta': 1
    }
    params['page'] = page
    response = requests.get(API_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch page {page}: {response}')
        return None

def check_data(dado):
    if isinstance(dado, dict):
        return {k: check_data(v) for k, v in dado.items()}
    elif dado == "":
        return None
    else:
        return dado

def save_to_database(data):
    session = SessionLocal()
    try:
        for d in data['rows']:
            row = check_data(d)
            if 'outras_classificacoes' in row:
                del row['outras_classificacoes']
            report = session.query(Report).filter_by(id_atendimento=row['id_atendimento']).first()
            if report:
                for key, value in row.items():
                    setattr(report, key, value)
            else:
                report = Report(**row)
                session.add(report)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    finally:
        session.close()

def main():
    while True:
        first_page_data = fetch_page(1)
        if not first_page_data:
            return

        total_pages = first_page_data['total']

        save_to_database(first_page_data)

        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(fetch_page, page) for page in range(2, total_pages + 1)]
            for future in futures:
                data = future.result()
                if data:
                    save_to_database(data)
        time.sleep(300)

if __name__ == '__main__':
    main()
