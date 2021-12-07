from urllib.request import urlopen
import time

start_time = time.time()

def get_content_len(url):
    response = urlopen(url)
    content = response.read()
    print(len(content))
urls = [
    "https://unm.ac.id",
    "https://unm.ac.id/identitas/",
    "https://syam-ok.unm.ac.id/",
    "http://ft.unm.ac.id/"
]

for url in urls:
    get_content_len(url)

print("Mengambil panjang halaman web sudah selesai...")

print("--- Waktu eksekusi program: %s detik ---" % (time.time() -
start_time))