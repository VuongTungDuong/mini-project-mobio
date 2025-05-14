# Dự án học giữa kafka và zookeeper

Tạo .venv

## Pdm để  quản lý phiên bản

Thêm pkg mới

```bash
uv add <pkg>
```

Đồng bộ lại môi trường và cái các pkg

```bash
uv sync
```

Kiểm tra cập nhật pkg và ghi vào file lock

```bash
uv lock
```

## Run

```bash
python app_journey_builder_api.py
```

## Test

```bash
python -m tests.test_email_post
```

## Chuyển sang py sang c

```bash
python setup.py build_ext --inplace
```
