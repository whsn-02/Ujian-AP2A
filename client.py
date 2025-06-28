import requests
import threading
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"
URLS_TO_CHECK = [
    f"{BASE_URL}/status/ok",
    f"{BASE_URL}/status/slow",
    f"{BASE_URL}/status/error",
    f"{BASE_URL}/status/nonexistent", # Ini akan menghasilkan 404
    f"{BASE_URL}/status/ok"
]
NUM_REQUESTS = len(URLS_TO_CHECK)
CLIENT_LOG_FILE = "health_check_log.txt"

client_log_lock = threading.Lock()

with open(CLIENT_LOG_FILE, "w", encoding="utf-8") as f:
    f.write(f"--- URL Health Check Log Started: {datetime.now()} ---\n")

# ==============================================================================
# SOAL 1: Implementasi Logging Thread-Safe
# ==============================================================================
def log_client_activity_safe(thread_name, message):
    """
    TUGAS ANDA (Soal 1):
    Lengkapi fungsi ini untuk mencatat 'message' dari 'thread_name' ke
    CLIENT_LOG_FILE secara thread-safe menggunakan 'client_log_lock'.

    Langkah-langkah:
    1. Dapatkan 'client_log_lock' (gunakan 'with' statement untuk kemudahan).
    2. Buat timestamp (contoh: datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")).
    3. Format pesan log (contoh: f"[{timestamp}] [{thread_name}] {message}\n").
    4. Tulis pesan log ke CLIENT_LOG_FILE (mode append 'a', encoding 'utf-8').
    5. (Opsional) Cetak pesan log ke konsol juga.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 1 DI SINI =====
    client_log_lock with
    datetime.now().strftime("f") 
 f"[{timestamp}] [{thread_name}] {mencatat thread_name}\n")
with open(CLIENT_LOG_FILE, "a", encoding="utf-8") as f:
     f.write(f"---URL Health Check Log Started:{datetime.now()})---\n") 
    
    
     
    # =================================================


# ==============================================================================
# SOAL 2: Implementasi Fungsi Pengecekan URL
# ==============================================================================
def check_url_health(url, current_thread_name):
    """
    TUGAS ANDA (Soal 2):
    Lengkapi fungsi ini untuk mengirim permintaan GET ke sebuah URL
    dan mencatat hasilnya menggunakan fungsi 'log_client_activity_safe' yang
    telah Anda implementasikan di Soal 1.

    Langkah-langkah:
    1. 'target_url' sudah diberikan sebagai parameter 'url'.
    2. Catat (menggunakan 'log_client_activity_safe') bahwa pengecekan akan dimulai.
    3. Gunakan blok 'try-except' untuk menangani potensi error saat request.
       a. Di dalam 'try':
          i.  Kirim permintaan GET ke 'url' menggunakan 'requests.get()'.
              Sertakan timeout yang singkat (misalnya, 2.5 detik) untuk mendeteksi endpoint yang lambat.
          ii. Periksa 'response.status_code':
              - Jika status code ada di rentang 200-299 (sukses):
                  - Catat pesan sukses. Contoh: f"SUKSES! URL {url} merespons dengan status {response.status_code}."
              - Jika tidak (misal 404, 500):
                  - Catat pesan kegagalan. Contoh: f"GAGAL! URL {url} merespons dengan status {response.status_code}."
       b. Di blok 'except requests.exceptions.Timeout':
          - Catat pesan timeout. Contoh: f"TIMEOUT! URL {url} tidak merespons dalam batas waktu."
       c. Di blok 'except requests.exceptions.RequestException as e':
          - Catat pesan error koneksi. Contoh: f"KONEKSI GAGAL! Tidak dapat terhubung ke {url}. Error: {e}"
       d. Di blok 'except Exception as e':
          - Catat pesan kesalahan tak terduga.
    4. Setelah blok try-except, catat bahwa pengecekan untuk URL ini selesai.
    """
    # ===== TULIS KODE ANDA UNTUK SOAL 2 DI SINI =====
thread_name = f"check_url_health--{url}"
log_client_activity_safe(thread_name, f"Memulai pengecekan untuk URL: {url}")
'try-except'methods =='GET': 
    try request.method == 'GET' 
    


    
    # =================================================

def worker_thread_task(url, task_id):
    """Fungsi yang dijalankan oleh setiap worker thread."""
    thread_name = f"Worker-{task_id}"
    log_client_activity_safe(thread_name, f"Memulai pengecekan untuk URL: {url}")
    check_url_health(url, thread_name)
    log_client_activity_safe(thread_name, f"Selesai pengecekan untuk URL: {url}")

if __name__ == "__main__":
    log_client_activity_safe("MainClient", f"Memulai {NUM_REQUESTS} pengecekan kesehatan URL secara concurrent.")
    
    threads = []
    start_time = time.time()

    for i, target_url in enumerate(URLS_TO_CHECK):
        thread = threading.Thread(target=worker_thread_task, args=(target_url, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    total_time = end_time - start_time
    
    log_client_activity_safe("MainClient", f"Semua pengecekan URL selesai dalam {total_time:.2f} detik.")
    print(f"\nLog aktivitas klien disimpan di: {CLIENT_LOG_FILE}")
    print(f"Total waktu eksekusi: {total_time:.2f} detik.")