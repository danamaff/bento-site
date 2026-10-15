# Сахарная коробочка

[![Проверка и публикация сайта](https://github.com/danamaff/bento-site/actions/workflows/deploy.yml/badge.svg)](https://github.com/danamaff/bento-site/actions/workflows/deploy.yml)

Лендинг кондитерской бенто-тортов «Сахарная коробочка».

Сайт: https://danamaff.github.io/bento-site/

## Как устроена публикация

При каждом изменении ветки `main` GitHub Actions запускает workflow `.github/workflows/deploy.yml`:

1. **Проверка HTML и ссылок** – HTMLHint проверяет разметку по правилам из файла `.htmlhintrc`, а скрипт `.github/scripts/check_links.py` проверяет, что ссылки на разделы и картинки ведут на существующие места.
2. **Публикация на GitHub Pages** – выполняется, только если проверка прошла без ошибок.

Для запросов на слияние (pull request) запускается только проверка, поэтому ошибка видна ещё до попадания изменений в `main`.

Значок вверху показывает результат последнего запуска: passing – всё в порядке, failing – найдена ошибка.
