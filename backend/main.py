import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from engine import query_engine
app = FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["*"])
@app.get('/stream_chat')
async def stream_chat(param:str = "你好"):
    # 我们假设query_engine已经构建完成
    response_stream = query_engine.query(param) 
    async def generate():  
        for text in response_stream.response_gen:
            yield text
    return StreamingResponse(generate(), media_type='text/event-stream')  
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)