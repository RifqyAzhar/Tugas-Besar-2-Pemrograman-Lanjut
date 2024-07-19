import mysql.connector
from buku import Buku

def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="perpustakaan"
    )
    return conn

def get_buku(buku_id):
    cursor = conn.cursor()
    query = "SELECT * FROM buku WHERE id = %s"
    cursor.execute(query, (buku_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result:
        return Buku(*result[1:])
    return None

def post_buku(buku):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, '\n'.join(buku.konten), buku.iktisar))
    conn.commit()
    cursor.close()
    conn.close()