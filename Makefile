default:
	echo "See README.md"

init:
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -r requirements.txt; \

load_data:
	source .venv/bin/activate; \
	python3 -m src.data.load_data_pipeline; \
	python3 -m src.data.remove_duplicates; \

train_xgb: data/housing_data.csv
	source .venv/bin/activate; \
	python3 -m src.models.xgb_train; \

app: models/xgb.pkl
	source .venv/bin/activate; \
	uvicorn app:app; \

app_dev: models/xgb.pkl
	source .venv/bin/activate; \
	uvicorn app:app --reload; \
