""" from app.models import db, File

def store_file_in_db(file_path: str, title: str):
    with open(file_path, "rb") as f:
        file_bytes = f.read()

    new_file = File(title=title)
    db.session.add(new_file)
    db.session.commit()

def read_file_lines(file_path: str) -> list[str]:
    lines = []
    try:
        with open(file_path, 'r') as reader:
            for line in reader:
                lines.append(line.strip())
    except IOError as e:
        raise IOError(f"I/O error while reading file: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error: {e}")
    return lines

 """