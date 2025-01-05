# Финальный проект 4 спринта курса "Автоматизатор тестирования на Python" от Яндекс Практикум на тему "Юнит-тестирование"Файлы:

## Файлы:
- conftest.py - вспомогательная функция (фикстура)
- main.py - класс BooksCollector
- tests.py - тестовый класс TestBooksCollector

## Набор тестовых методов класса TestBooksCollector:
1. test_add_new_book_adding_three_books_success: Проверка добавления трех книг в словарь books_genre
2. test_add_new_book_check_genre_success: Проверка установления жанра по умолчанию в добавленной книге
3. test_add_new_book_add_incorrect_name_not_added: Негативная проверка добавления книг с именем 0 и больше 40 символов
4. test_add_new_book_add_double_books_not_added: Негативная проверка повторного добавления одинаковых книг
5. test_set_book_genre_added: Проверка добавления жанра из списка genre книге из списка books_genre
6. test_set_book_genre_changed: Проверка изменения жанра из списка genre книге из списка books_genre
7. test_set_book_genre_missing_genre_not_added: Негативная проверка добавления жанра не из списка genre книге из списка books_genre
8. test_get_books_with_specific_genre_success: Проверка вывода книги определенного жанра
9. test_get_books_with_specific_genre_missing_book: Негативная проверка вывода отсутствующей книги определенного жанра
10. test_get_books_for_children_success: Проверка вывода списка книг с жанром для детей
11. test_add_book_in_favorites_add_one_book_added: Проверка добавления книги из списка books_genre в избранное
12. test_add_book_in_favorites_add_missing_book_not_added: Негативная проверка добавления книги не из списка books_genre в избранное
13. test_add_book_in_favorites_add_double_books_not_added: Негативная проверка повторного добавления книги в избранное
14. test_delete_book_from_favorites_book_deleted: Проверка удаления книги из списка избранное
15. test_delete_book_from_favorites_missing_book_not_deleted: Негативная проверка удаления книги не из списка избранное

### Команда для запуска тестов
`pytest -v tests.py`

### Команда для оценки покрытия
`pytest --cov=main`

### Команда для подробной оценки покрытия с учетом ветвления
`pytest --cov=main --cov-branch --cov-report=html`

### Результат выполнения 16 тестов: 100%
### Результат оценки покрытия с учетом ветвлений: 100%