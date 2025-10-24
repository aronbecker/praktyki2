from backend.models.category import Category
from backend.models.extensions import db
from .utils import getCategoryFromPkd

def getCattegories(row):
    codes = []
    categories = set()

    codes.append(str(row["GlownyKodPkd"]))
    for p in str(row["PozostaleKodyPkd"]).split("$##$"):
      codes.append(p)

    for c in codes:
      cat = getCategoryFromPkd(c)
      if (cat != ""):
        categories.add(cat)


    categoriesEntities = []

    for name in categories:
        name = name.strip()
        category = Category.query.filter_by(name=name).first()
        if not category:
            category = Category(name=name)
        categoriesEntities.append(category)

    return categoriesEntities
         
      