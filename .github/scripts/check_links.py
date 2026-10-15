"""Проверка ссылок сайта перед публикацией.

Для каждой HTML-страницы проверяет, что:
- ссылки вида #раздел ведут на существующий id на странице;
- локальные файлы (картинки и другие страницы) есть в репозитории.
"""
import os
import re
import sys

errors = 0
for page in sys.argv[1:]:
    html = open(page, encoding="utf-8").read()
    ids = set(re.findall(r'\sid="([^"]+)"', html))
    folder = os.path.dirname(page)
    links = re.findall(r'\s(?:href|src)="([^"]+)"', html)
    for link in links:
        if link.startswith("#"):
            # "#" и "#top" по стандарту HTML ведут в начало страницы
            if link not in ("#", "#top") and link[1:] not in ids:
                print(f"ОШИБКА {page}: ссылка {link} ведёт на несуществующий раздел")
                errors += 1
        elif not re.match(r"^(https?:|mailto:|tel:|data:)", link):
            if not os.path.exists(os.path.join(folder, link)):
                print(f"ОШИБКА {page}: файл {link} не найден в репозитории")
                errors += 1
    print(f"{page}: проверено ссылок – {len(links)}, ошибок – {errors}")

sys.exit(1 if errors else 0)
