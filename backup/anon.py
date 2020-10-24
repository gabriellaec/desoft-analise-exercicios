from pathlib import Path


BASE_DIR = Path(__file__).parent

for i, user_dir in enumerate(BASE_DIR.glob('user_*'), 1):
    if not user_dir.is_dir():
        continue
    user_dir.rename(BASE_DIR / f'user_{i:03d}')
