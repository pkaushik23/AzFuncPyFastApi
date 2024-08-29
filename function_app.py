import asyncio
import azure.functions as func
import logging
from azurefunctions.extensions.http.fastapi import Request, StreamingResponse, Response, JSONResponse

import copilot.copilot as copilot

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="HttpExample")
async def HttpExample(req: Request) -> Response:
    logging.info('Python HTTP trigger function processed a request.')
    # cors_setting = os.getenv('CORS')
    # logging.info(cors_setting)
    name = req.get('name')
    if not name:
        try:
            req_body = await req.json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name: 
        response = copilot.answer_the_question(name)
        return Response(status_code=200,content=response.content)
    else:
        return Response(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )



async def stream_processor(response):
    async for chunk in response:
        #print(f"Extracted content: \n{chunk}")
        await asyncio.sleep(0.1)
        yield chunk.content
        # if len(chunk.choices) > 0:
        #     delta = chunk.choices[0].delta
        #     if delta.content: # Get remaining generated response if applicable
        #         await asyncio.sleep(0.1)
        #         yield delta.content

@app.route(route="HttpExampleStreamed")
async def HttpExampleStreamed(req: Request) -> StreamingResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # cors_setting = os.getenv('CORS')
    # logging.info(cors_setting)
    question = req.get('question')
    if not question:
        try:
            req_body = await req.json()
        except ValueError:
            pass
        else:
            question = req_body.get('question')
    if not question:
        question = "Please tell me a interesting fact in 200 words"
    if question: 
        response = copilot.answer_the_question(question, True)
        return StreamingResponse(stream_processor(response), media_type="text/event-stream")
    else:
        return Response(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

