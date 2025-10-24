from backend.models.extensions import db
import pandas as pd
from .utils import getCategoryFromPkd

def import_kategori(data):
  for i, row in data.iterrows():
      codes = []

      codes.append(row["GlownyKodPkd"])
      for p in row["PozostaleKodyPkd"].split("$##$"):
        codes.append(p)

      getCategoryFromPkdromPkd()
      