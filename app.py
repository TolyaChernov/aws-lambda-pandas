import pandas as pd
import json


def lambda_handler(event, context):
    body = json.loads(event['body'])
    df = pd.DataFrame([body])

    # запись
    filename = '/tmp/output.json'
    df.to_json(filename, orient="records")

    # чтение и печать для проверки работы функции
    with open(filename, 'r') as file:
        data = json.load(file)
        print('===', data, '===', df)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Данные сохранены: {filename}'})
    }
