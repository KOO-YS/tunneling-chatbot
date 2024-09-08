
### `.venv` 경로에 가상 환경, 종속성이 설치
```python
python -m venv .venv
```

### 가상환경 활성화
```
# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```

### 가상환경 비활성화
```
deactivate
```

```

pip install streamlit

# 정상 설치 테스트 1
streamlit hello

# 정상 설치 테스트 2
python -m streamlit hello

pip install -r requirements.txt
```

---

### app.py를 메인으로 애플리케이션 시작
```
streamlit run app.py
```

### Gemini api key 등록 

```
# Windows command prompt
setx GOOGLE_API_KEY "발급받은 API KEY"

# macOS and Linux
echo 'export GOOGLE_API_KEY='"발급받은 API KEY"' >> ~/.bashrc
```