from backend.models.category import Category
from backend.models.keyword import Keyword
from backend.models.extensions import db
from .utils import getKeywordFromCategory


def import_slow_kluczowych():
    categories = Category.query.all()

    for c in categories:
        name = c.name
        keywords = getKeywordFromCategory(name)

        keywordsEntities = []
        for k in keywords:
            keyword = Keyword.query.filter_by(keyword=k).first()
            if not keyword:
                keyword = Keyword(keyword = k, category_id = c.id)
            keywordsEntities.append(keyword)

        c.keywords = keywordsEntities
        db.session.commit()

        