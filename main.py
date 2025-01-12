from fastapi import FastAPI
import pandas as pd


app = FastAPI()

def load_surahs():
    
    file_path = "UrduTranslationsFatehMuhammadAndShaikhulHind.xlsx"
    df = pd.read_excel(file_path)
    return df

quran_data = load_surahs()


@app.get("/")
async def root():
    return {"message": "Welcome to the Quran Surah API"}

# Get all Surah Names
@app.get("/surah/names")
async def get_all_surah_names():
    surah_names_arabic = quran_data["SurahNameU"].drop_duplicates().tolist()
    surah_names_english = quran_data["SurahNameE"].drop_duplicates().tolist()
    return {
        "All Surah Names in Arabic": surah_names_arabic,
        "All Surah Names in English": surah_names_english
        }

# Get Surah by ID
@app.get("/surah/{sura_id}")
async def get_surah_by_id(sura_id: int):
    surah = quran_data[quran_data["SuraID"] == sura_id]
    if surah.empty:
        return {"error": f"Surah with ID {sura_id} not found"}
    return {"Surah Name": surah.iloc[0]["SurahNameU"]}

# Get a Translation by Surah ID
@app.get("/surah/{sura_id}/arabictext")
async def get_translation(sura_id: int):
    surah = quran_data[quran_data["SuraID"] == sura_id]
    if surah.empty:
        return {"error": f"Surah with ID {sura_id} not found"}
    return {
        "Surah Name": surah.iloc[0]["SurahNameU"],
        "Arabic Text": surah["Arabic Text"].tolist()
    }

# Get a Translation of Fateh Muhammad Jalandhri by Surah ID
@app.get("/surah/{sura_id}/fateh-muhammad-jalandhri")
async def get_translation(sura_id: int):
    surah = quran_data[quran_data["SuraID"] == sura_id]
    if surah.empty:
        return {"error": f"Surah with ID {sura_id} not found"}
    return {
        "Surah Name": surah.iloc[0]["SurahNameU"],
        "Translation Fateh Muhammad Jalandhri": surah["Fateh Muhammad Jalandhri"].tolist()
    }

# Get a Translation of Mehmood ul Hassan by Surah ID
@app.get("/surah/{sura_id}/mehmood-ul-hassan")
async def get_translation(sura_id: int):
    surah = quran_data[quran_data["SuraID"] == sura_id]
    if surah.empty:
        return {"error": f"Surah with ID {sura_id} not found"}
    return {
        "Surah Name": surah.iloc[0]["SurahNameU"],
        "Translation Mehmood ul Hassan": surah["Mehmood ul Hassan"].tolist()
    }

# To run this code, save it as main.py and run the following command:
# uvicorn main:app --reload