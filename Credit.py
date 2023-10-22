from pydantic import BaseModel
class Credit(BaseModel):
    isMustahiq: int
    UMR_Provinsi: int
    Untung_Kotor: int
    Pengeluaran: int
    Untung_Bersih: int
    Presentase_Serapan_Pasar: float
    Sustain: int
    isInfra: int
    isIZIN: int
    Nominal_Kebutuhan_Alat: int
    
   