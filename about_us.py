from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()

# # Пример данных
# fake_items_db = [{"item_name": "Товар 1"}, {"item_name": "Товар 2"}, {"item_name": "Товар 3"}]

prepared_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore."
prepared_text2 = "Lorem ipsum dolor sit amet"

text_title = "We Create Digital World Class Business Agency Marketplace"
text_subtitle = "About us",


@app.get("/get_info/{id}")
async def get_info(id: int):
    if id == 1:
        return {"title": text_title}
    elif id == 2:
        return {"subtitle": text_subtitle}
    else:
        raise HTTPException(status_code=404, detail="Данных по такому запросу не существует")

# # Эндпоинт для получения данных
# @app.get("/items/")
# async def read_items():
#     return fake_items_db


# Эндпоинт для получения изображений
image_directory = "C:\\Users\\Donish\\Desktop\\fastap\\assets"

@app.get("/images/{image_name}")
async def get_image(image_name: str):
    image_path = os.path.join(image_directory, image_name)
    
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Изображение не найдено")
    
    return FileResponse(image_path)
    



# Эндпоинт для получения заготовленного текста
@app.get("/get_prepa    red_text/{id}")
async def get_prepared_text(id: int):
    if id == 1:
        return {"text": prepared_text}
    if id == 2:
        return {"text": prepared_text2}
    else:
        raise HTTPException(status_code=404, detail="Текст c указанным идентификатором не найден")
    