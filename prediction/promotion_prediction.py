from pydantic import BaseModel

class PromotionPrediction(BaseModel):
    wilayah: str
    pendidikan: str
    jenis_kelamin: str
    jumlah_training: int
    umur: int
    rating_tahun_lalu: int
    masa_kerja: int
    KPI: str
    penghargaan: str
    rata_rata_skor_training: int
    departemen: str
    rekrutmen: str