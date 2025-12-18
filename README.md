
# Лабораторные работы по Архитектуре ПО

**Студентка:** Пестова Виктория Рафаиловна, РИ-330935

---

### lab1
Приложение для получения IP-адреса в формате JSON.
Выбор API (`ip-api` или `jsonip`) настраивается через переменную `TYPE` в файле `.env`.
<img width="409" height="91" alt="image" src="https://github.com/user-attachments/assets/f60161dc-6b60-4c04-bdff-660c17b43b96" />

**Запуск:**
```bash
cd lab1
docker compose up --build
```
<img width="333" height="132" alt="image" src="https://github.com/user-attachments/assets/49f05599-da02-49ea-8641-6e3c595c9f91" />
<img width="330" height="142" alt="image" src="https://github.com/user-attachments/assets/33620ba8-b554-41b1-a48c-276a5cd9f768" />
Логи запуска
<img width="942" height="228" alt="image" src="https://github.com/user-attachments/assets/4bac3f33-e9f1-4ca5-9132-0514074955e0" />


---

### lab2
Веб-приложение "Список задач" с использованием Flask и Redis.
Демонстрирует подключение внешнего хранилища (Redis) в Docker Compose.

**Запуск:**
```bash
cd lab2
docker compose up --build
```
<img width="1357" height="461" alt="image" src="https://github.com/user-attachments/assets/ea03ace0-cbdb-4839-b1ab-c950cc1de680" />
Логи запуска
<img width="972" height="195" alt="image" src="https://github.com/user-attachments/assets/f5cbf0e5-6f95-498d-8968-7fd158510e6f" />

Скриншот работающих контейнеров из Docker Desktop ДЛЯ ЛАБОРАТОРНЫХ 1 И 2 
<img width="925" height="236" alt="image" src="https://github.com/user-attachments/assets/45d88b01-3bde-4f3c-aadd-d166047f15a6" />:
---

### lab3
Конфигурационные файлы (`Deployment`, `Service`) для развертывания приложения в Kubernetes.



