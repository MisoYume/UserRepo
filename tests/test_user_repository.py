import unittest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.user import Base
from repositories.user_repository import UserRepository


class TestUserRepository(unittest.TestCase):
    
    def setUp(self):
        """
        Подготовка перед КАЖДЫМ тестом
        """
        self.engine = create_engine("postgresql://postgres:postgres@localhost:5432/test_db")
        Base.metadata.drop_all(bind=self.engine)
        Base.metadata.create_all(bind=self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)
        self.db = self.SessionLocal()
        self.repo = UserRepository(self.db)

    
    def tearDown(self):
        """
        Очистка после КАЖДОГО теста  
        """
        self.db.close()
    
    def test_create_user(self):
        """
        Тест создания пользователя
        """
        name, surname, weight, birth_date = "Иван", "Иванов", 73.6, date(1990, 1, 15)
        user = self.repo.create_user(name, surname, weight, birth_date)

        self.assertIsNotNone(user.user_id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.surname, surname)
        self.assertEqual(user.weight, weight)
        self.assertEqual(user.birth_date, birth_date)
    
    def test_get_user_by_id(self):
        """
        Тест поиска пользователя по ID
        """
        user = self.repo.create_user("Александра", "Александровна", 54.2, date(2000, 7, 7))
        found_user = self.repo.get_user_by_id(user.user_id)

        self.assertEqual(found_user.user_id, user.user_id)
        self.assertEqual(found_user.name, "Александра")
        self.assertEqual(found_user.surname, "Александровна")
        self.assertEqual(found_user.weight, 54.2)
        self.assertEqual(found_user.birth_date, date(2000, 7, 7))

        not_found = self.repo.get_user_by_id(99999)
        self.assertIsNone(not_found)
    
    def test_get_all_users(self):
        """
        Тест вывода списка всех пользователей
        """
        empty_users = self.repo.get_all_users()
        self.assertEqual(len(empty_users), 0)

        user1 = self.repo.create_user("Наруто", "Узумаки", 60.5, date(2006, 8, 4))
        user2 = self.repo.create_user("Саске", "Учиха", 63.5, date(2006, 7, 5))

        all_users = self.repo.get_all_users()

        self.assertEqual(len(all_users), 2)
        self.assertIn(user1, all_users)
        self.assertIn(user2, all_users)

    def test_get_users_by_name(self):
        """
        Тест  пользователя по его имени и фамилии
        """
        user1 = self.repo.create_user("Наруто", "Узумаки", 60.5, date(2006, 8, 4))
        user2 = self.repo.create_user("Наруто", "Учиха", 63.5, date(2006, 7, 5))
        user3 = self.repo.create_user("Саске", "Учиха", 65.5, date(2005, 7, 5))

        found_user = self.repo.get_users_by_name("Наруто", "Узумаки")

        self.assertEqual(len(found_user), 1)
        self.assertEqual(found_user[0].user_id, 1)

        not_found = self.repo.get_users_by_name("Несуществующий", "Пользователь")
        self.assertEqual(len(not_found), 0)
    
    def test_update_user(self):
        """
        Тест обновления данных пользователя
        """
        user = self.repo.create_user("Сакура", "Харуно", 48, date(2006, 6, 5))

        updated_user = self.repo.update_user(
            user.user_id,
            surname = "Учиха",
            weight = 46.5
        )

        self.assertEqual(updated_user.surname, "Учиха")
        self.assertEqual(updated_user.weight, 46.5)

        not_updated = self.repo.update_user(99999, name="Test")
        self.assertIsNone(not_updated)

    def test_delete_user(self):
        """
        Тест на удаление пользователя
        """
        user = self.repo.create_user("Какаши", "Хатаке", 74, date(1995, 4, 3))

        deleted_user = self.repo.delete_user(user.user_id)

        self.assertTrue(deleted_user)

        found_after_delete = self.repo.get_user_by_id(user.user_id)
        self.assertIsNone(found_after_delete)

        delete_non_existent = self.repo.delete_user(99999)
        self.assertFalse(delete_non_existent)


if __name__ == '__main__':
    unittest.main()