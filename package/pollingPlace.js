const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })
const s3 = new AWS.S3()

exports.handler = async (event) =>{
    const result = await getUploadURL()
    console.log('Result: ', result)
    return result
}

const getUploadURL = async function(){
  const randomId = parseInt(Math.random()*10000000000)
    
  const s3Params = {
    Bucket: process.env.UploadBucket,
    Key: `${randomId}.jpg`,
    ContentType: 'image/jpeg',
    ACL: 'public-read'
  }

  console.log('getUploadURL: ', s3Params)
  return new Promise((resolve, reject) => {
    resolve({
      "statusCode": 200,
      "isBase64Encoded": false,
      "headers":{
        "Access-Control-Allow-Origin": "*"
    },
    "body": JSON.stringify({
        "uploadURL": s3.getSignedUrl('putObject', s3Params),
        "photoFilename": `${randomId}.jpg`
     })
   })
 })
} 

'use strict'

const AWS = require('aws-sdk')
AWS.config.update({ region: process.env.AWS_REGION })
const s3 = new AWS.S3()

const URL_EXPIRATION_SECONDS = 300

exports.handler = async (event) => {
  return await getUploadURL(event)
}

const getUploadURL = async function(event) {
  const randomID = parseInt(Math.random() * 10000000)
  const Key = `${randomID}.jpg`

  const s3Params = {
    Bucket: process.env.UploadBucket,
    Key,
    Expires: URL_EXPIRATION_SECONDS,
    ContentType: 'image/jpeg',
  }

  console.log('Params: ', s3Params)
  const uploadURL = await s3.getSignedUrlPromise('putObject', s3Params)

  return JSON.stringify({
    uploadURL: uploadURL,
    Key
  })
}

