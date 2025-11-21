from sqlalchemy.orm import Session
from models.user import User
from typing import List, Optional

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, name: str, surname: str, weight: float, birth_date: str) -> User:
        """
        Создает нового пользователя в базе данных
        """
        user = User(
            name=name,
            surname=surname,
            weight=weight,
            birth_date=birth_date
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """
        Выводит определенного пользователя по его id
        """
        user = self.db.query(User).filter(User.user_id == user_id).first()
        return user

    def get_all_users(self) -> List[User]:
        """
        Выводит список всех пользователей
        """
        users = self.db.query(User).all()
        return users

    def get_users_by_name(self, name: str, surname: str) -> List[User]:
        """
        Выводит пользователя по его имени и фамилии
        """
        users = self.db.query(User).filter(
            User.name == name, 
            User.surname == surname
        ).all()
        return users
    
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        """
        Обновляет данные пользователя
        """
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):  
                    setattr(user, key, value)

            self.db.commit()
            self.db.refresh(user)
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        """
        Удаляет пользователя
        """
        user = self.db.query(User).filter(User.user_id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False

