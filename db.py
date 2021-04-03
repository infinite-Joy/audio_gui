"""
CREATE TABLE sylheti_text(
  "Text" TEXT,
  "audio_file" TEXT
);
"""

import sqlite3

TABLENAME = 'sylheti_text'
db_file = "db.sqlite3"

def read_not_done_text_from_table():
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        rows = []
        for row in cur.execute(f'SELECT ROWID, * FROM {TABLENAME} where audio_file=""'):
            rows.append(row)

        return rows

def update_table_for_done_text(rowid, filename):
    with sqlite3.connect(db_file) as con:
        cur = con.cursor()
        res = cur.execute(f"update {TABLENAME} set audio_file='{filename}' where ROWID={rowid};")
        con.commit()


if __name__ == '__main__':
    table = read_not_done_text_from_table()
    print(table[0])

    update_table_for_done_text(2, "filename")