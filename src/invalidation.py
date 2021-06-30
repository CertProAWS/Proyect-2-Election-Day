import json
import boto3
import os

from boto3.dynamodb.conditions import Key, Attr

MyInvalidationTable = os.environ['MyInvalidationTable']
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(MyInvalidationTable)


def getInvalid(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    invalid = path.split("/")[-1] # ["user", "id"]
    response = table.scan(
        FilterExpression=Attr('invalido').true
    )

    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }

def putInvalid(event, context):
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

def getCity(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    cabina_id = path.split("/")[-1] # ["user", "id"]
    city = path.split("/")[-3] # ["user", "id"]
    body = json.loads(event["body"])
    response = table.scan(
        FilterExpression=Attr('city').body(city)
        
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("item")
    }
def putCity(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    city = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(city)
    item = {
        'pk': city,
        'sk': 'info',
        #'room_list': body["room_list"],

     }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
def getSchool(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    school = path.split("/")[-1] # ["user", "id"]
    response = table.scan(
        FilterExpression=Attr('school').body(school)
    )
    item = response['Item']
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
    
    

def putSchool(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    path = event["path"]
    school = path.split("/")[-1] # ["user", "id"]
    
    body = json.loads(event["body"])
    print(body)
    print(school)
    item = {
        'pk': school,
        'sk': 'info',
        #'room_list': body["room_list"],

    }
    print(json.dumps(item))
    table.put_item(
      Item=item
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }