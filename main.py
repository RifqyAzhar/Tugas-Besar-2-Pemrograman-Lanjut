from buku import Buku
from database import connect_db, get_buku, post_buku
from logger import log_buku, logger

if __name__ == "__main__":
    contoh_buku = Buku(
        judul="Pemrograman Java untuk Pemula",
        penulis="Bambang Hariyanto",
        penerbit="Elex Media Komputindo",
        tahun_terbit=2010,
        konten=["Bab 1: Pengenalan Java", "Bab 2: Dasar-dasar Pemrograman Java", "Bab 3: Array dan Koleksi", "Bab 4: Pemrograman Berorientasi Objek", "Bab 5: Database dengan JDBC"],
        iktisar="Buku ini memberikan dasar-dasar pemrograman Java dengan penjelasan yang mudah dipahami dan banyak contoh praktis. Cocok untuk pemula yang ingin mempelajari Java."
    )

    print(contoh_buku)
    contoh_buku.read(2)
    log_buku(contoh_buku)

    conn = connect_db()

    buku_id = post_buku(conn, contoh_buku)
    logger.info(f"Buku berhasil disimpan ke database: {buku_id}")

    buku_dari_db = get_buku(conn, buku_id)
    if buku_dari_db:
        print(buku_dari_db)
    else:
        logger.error("Buku tidak ditemukan di database")