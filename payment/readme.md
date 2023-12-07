instructions on gettings setup

## Usage

### Creating a virtual environment

```bash
python -m venv venv
```

### Activating the virtual environment

```bash
.\venv\Scripts\activate # Windows
source venv/bin/activate # Linux
```

### Installing dependencies

```bash
pip install -r requirements.txt
```

### Running the application

```bash
uvicorn main:app --reload
```
