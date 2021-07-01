import json
import boto3
import os

from boto3.dynamodb.conditions import Key, Attr

voters_table = os.environ['VOTERS_TABLE']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(voters_table)

def getVoter(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    voter_id = path.split("/")[-1] 
    response = table.get_item(
        Key={
            'pk': voter_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }


def putVoter(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    voter_id = path.split("/")[-1] # ["user", "id"]
    body = json.loads(event["body"])
    print(body)
    print(voter_id)
    item = {
        'pk': voter_id,
        'sk': 'info',
        'name_voter': body["name_voter"],
        'city': body["city"],
        'school': body["school"],
        'booth': body["booth"],
        'timeOfArrival': body["timeOfArrival"],
        'country': body["country"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
def getAbsentee(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    absentee_id = path.split("/")[-1]
    response = table.get_item(
        Key={
            'pk': absentee_id,
            'sk': 'info'
        }
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putAbsentee(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    absentee_id = path.split("/")[-1] # ["user", "id"]
    body = json.loads(event["body"])
    print(body)
    print(absentee_id)
    item = {
        'pk': absentee_id,
        'sk': 'info',
        'absentee' : body["absentee"],
        'name_voter': body["name_voter"],
        'city': body["city"],
        'school': body["school"],
        'booth': body["booth"],
        'country': body["country"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def getInvalidFunction(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    invalid = path.split("/")[-1] # ["user", "id"]
    response = table.scan(
        FilterExpression=Attr('invalido').eq(True)
    )

    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

def putInvalidFunction(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    cabina_id = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(cabina_id)
    item = {
        'pk': cabina_id,
        'invalido': body["invalido"],
        'city': body["city"],
        'school': body["school"],
        'resultadoImagen': body["resultadoImagen"],
        'resultadoFinal': body["resultadoFinal"],
        'ausentes': body["ausentes"],
        'votosEmitidos': body["votosEmitidos"],
        'votosTotales': body["votosTotales"]
    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }    


