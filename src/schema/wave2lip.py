from pydantic import BaseModel
from typing import List, Optional

class InputWave2lip(BaseModel):
    checkpoint_path: str
    face_path: str
    audio_path: str

class ResultWave2lip:
    outfile: str

class OutputWave2lip:
    success: bool
    message: str
    data: Optional[ResultWave2lip]


