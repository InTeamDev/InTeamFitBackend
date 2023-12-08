import io

import numpy as np
from PIL import Image
from fastapi import APIRouter, HTTPException, Depends
from fastapi import File, UploadFile

from app.schemas.equipment import Equipment
from app.services.equipment import EquipmentService
from model.model import ModelManager, get_model_manager


equipment_router = APIRouter()


@equipment_router.post("/equipment/predict", response_model=list[Equipment])
async def predict_image(file: UploadFile = File(...), model_manager: ModelManager = Depends(get_model_manager)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    image_array = np.array(image)
    image_array /= 255.0  # модель работает с числами от 0 до 1, поэтому все значения приведём к этому диапазону
    return await EquipmentService.recognize(image_array, model_manager.get_model())
    # try:
    #
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
