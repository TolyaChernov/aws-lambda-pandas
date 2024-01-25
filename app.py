import pandas as pd
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        # лог запроса
        logging.info(f'Event: {event}')
        logging.info(f'Context: {context}')
        logging.info(f'Body: {event["body"]}')
        logging.info(f'Headers: {event["headers"]}')
        logging.info(f'QueryStringParameters: {event["queryStringParameters"]}')
        logging.info(f'PathParameters: {event["pathParameters"]}')
        logging.info(f'StageVariables: {event["stageVariables"]}')
        logging.info(f'IsBase64Encoded: {event["isBase64Encoded"]}')
        logging.info(f'RequestContext: {event["requestContext"]}')
        logging.info(f'Resource: {event["resource"]}')
        logging.info(f'HttpMethod: {event["httpMethod"]}')
        logging.info(f'ApiId: {event["requestContext"]["apiId"]}')
        logging.info(f'Identity: {event["requestContext"]["identity"]}')
        body = json.loads(event['body'])
        df = pd.DataFrame([body])
        logging.info(f'DataFrame: {df}')

        # запись данных в файл
        filename = '/tmp/output.json'
        df.to_json(filename, orient="records")
        logging.info(f'Write data: {df}')

        # чтение данных из файла
        with open(filename, 'r') as file:
            data = json.load(file)
            logging.info(f'Read data: {data}')

        return {
            'statusCode': 200,
            'body': json.dumps({'message': f'Data saved: {filename}'})
        }
    except Exception as e:
        logger.error(f'An error occurred: {str(e)}', exc_info=True)

        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'An error occurred during data processing', 'error': str(e)})
        }
