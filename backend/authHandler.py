from models.user import User
from models import Session

class AuthenticationResult:
    isAuthenticated: bool
    session: Session | None

    def __init__(self, isAuthenticated, session):
        self.isAuthenticated = isAuthenticated
        self.session = session

def authenticate(request) -> AuthenticationResult:
    session_id = request.cookies.get('session_id')

    result = AuthenticationResult(False, None)

    if not session_id:
        return result

    session = Session.query.filter_by(session_id=session_id).first()

    if not session:
        return result
    
    result.isAuthenticated = True
    result.session = session
    return result

def isAdmin(user: User) -> bool:
    return user.role == "admin"
