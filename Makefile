UNAME := $(shell uname)

default:
	echo "See README.md"

ifeq ($(OS), Windows_NT)
init: windows_init
load_data: windows_load_data
train_xgb: windows_train_xgb
app: windows_app
app_dev: windows_app_dev
else
init: linux_init
load_data: linux_load_data
train_xgb: linux_train_xgb
app: linux_app
app_dev: linux_app_dev
endif

linux_init:
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -r requirements.txt; \

linux_load_data:
	source .venv/bin/activate; \
	python3 -m src.data.load_data_pipeline; \
	python3 -m src.data.remove_duplicates; \

linux_train_xgb: data/housing_data.csv
	source .venv/bin/activate; \
	python3 -m src.models.xgb_train; \

linux_app: models/xgb.pkl
	source .venv/bin/activate; \
	uvicorn app:app; \

linux_app_dev: models/xgb.pkl
	source .venv/bin/activate; \
	uvicorn app:app --reload; \


windows_init:
	python -m venv .venv; \
	source .venv/Scripts/activate; \
	pip install -r requirements.txt; \

windows_load_data:
	source .venv/Scripts/activate; \
	python -m src.data.load_data_pipeline; \
	python -m src.data.remove_duplicates; \

windows_train_xgb: data/housing_data.csv
	source .venv/Scripts/activate; \
	python -m src.models.xgb_train; \

windows_app: ./models/xgb.pkl
	source .venv/Scripts/activate; \
	uvicorn app:app; \

windows_app_dev: models/xgb.pkl
	source .venv/Scripts/activate; \
	uvicorn app:app --reload; \
