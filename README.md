# Projects control RAG

Краткое описание приложения.

## Установка и Запуск

Следуйте этим инструкциям, чтобы установить зависимости и запустить приложение на разных операционных системах.

### Предварительные требования

- Установленный Python (рекомендуемая версия: 3.x)
- Установленный pip (обычно устанавливается вместе с Python)
- Ollama
  

### Общие шаги

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/IIT-student-apps/pydantic-projects-control-rag.git
   cd ваш-репозиторий

2. **Создание виртуального окружения и установка зависимостей**:
 
   2.1 **Для Windows**:
   
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

     
    2.2 **Для Linux**:
  
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    
    2.3 **Для macOS**:
  
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    2.4 **Установка зависимостей из requirements.txt**:
    ```bash
    pip install -r requirements.txt
   ```
3. **Установка Ollama**:


   3.1 **Для macOS**:
      
      [Download](https://ollama.com/download/Ollama-darwin.zip)
      
   3.2 **Для Windows**:
      
      [Download](https://ollama.com/download/OllamaSetup.exe)
      
   3.3 **Для Linux**:
      
      ```shell
      curl -fsSL https://ollama.com/install.sh | sh
      ```
5. **Запуск приложения**:
   ```bash
   cd app
   uvicorn main:app --reload   
