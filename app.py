from fastapi import FastAPI, File, UploadFile
import os
app = FastAPI()

@app.post("/tab-to-pipe")
async def tab_to_pipe(file: UploadFile = File(...)):
    pipe_file_path = f"{(file.filename)[:-4]}_pipe_converted.txt"
    contents = await file.read()
    converted_contents = contents.decode('utf-8-sig').replace('\t', '|')
    with open(pipe_file_path, 'w') as pipe_file:
        pipe_file.write(converted_contents)
        x = (f"{os.getcwd()}\{pipe_file_path}").replace("\\", "/")
    return {"status": "file converted to pipe SUCCESSFULLY",
            "file_location": x
            }


