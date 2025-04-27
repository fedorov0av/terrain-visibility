# terrain-visibility

Инструмент для расчёта зоны видимости на местности по матрице высот, координатам станции и радиусу обзора. Результат — полигон в формате GeoJSON.

## 🧩 Возможности

- Загрузка матрицы высот из файла (CSV)
- Определение зоны видимости станции по её координатам, высоте и радиусу обзора
- Генерация полигона доступной к обзору области в формате **GeoJSON**
- Визуализация результата во фронтенде (Vue.js)
- REST API на FastAPI

---

## ⚙️ Установка и запуск

Клонируйте репозиторий:

```bash
git clone https://github.com/fedorov0av/terrain-visibility.git
cd terrain-visibility
```

### 🔧 Зависимости

Убедитесь, что у вас установлен Python >= 3.7, Node.js >= 22, npm >= 10 (для фронтенда).

Рекомендуется использовать виртуальное окружение для Python. Например:

```bash
python3 -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

Затем установите зависимости:

```bash
pip install -r requirements.txt
```

### Конфигурация

Конфигурационный файл находится по пути: `backend/setup/config.yaml`

Пример содержимого:

```yaml
file_elevation_matrix: backend/files/input/alt.csv
file_output: backend/files/output/poligon.json
matrix_size:
  width: 50
  height: 50
```

### Запуск

#### 1. Консольное приложение

Выполните команду:

```bash
python3 app.py -x 47 -y 0 -H 1 -r 4
```

Результатом будет GeoJSON-файл с зоной обзора, сохранённый на диск по пути: `backend/files/output/poligon.json`

#### 2. Backend (FastAPI)

Запустите сервер:

```bash
uvicorn backend.app:app --port 8080
```

#### 3. Frontend (Vue.js)

В отдельном терминале установите зависимости и запустите проект:

```bash
cd frontend
npm install
npm run dev
```

Откройте http://localhost:5173 в браузере для интерфейса пользователя.
