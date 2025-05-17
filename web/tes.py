import requests
from bs4 import BeautifulSoup

# Fungsi untuk melakukan scraping dan mencari kata tertentu
def check_word_in_page(url, word):
    # Menambahkan header User-Agent untuk membuat permintaan terlihat seperti berasal dari browser biasa
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Mengambil halaman HTML dengan header
    response = requests.get(url, headers=headers)

    # Mengecek apakah request berhasil (status code 200)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Mengambil semua teks dari halaman
        text = soup.get_text()
        
        # Mengecek apakah kata yang dicari ada di teks halaman
        if word in text:
            return True
        else:
            return False
    else:
        return False

# Daftar URL untuk dicari
# urls = [
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-1',   # Link 1
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-101',   # Link 1
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-201',  # Link 2
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-301',  # Link 3
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-401',  # Link 4
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-501',  # Link 5
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N5-601'  # Link 6
    
#     # 'https://tes10.com'  # Link 10
# ]

# urls = [
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N4-1',   # Link 1
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N4-101',   # Link 1
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N4-201',  # Link 2
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N4-301',  # Link 3
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N4-401',  # Link 4
#     'https://www.kanshudo.com/collections/wikipedia_jlpt/WPJLPT-N4-501',  # Link 5
# ]
# urls = [
#     'https://www.kanshudo.com/collections/iknow/IK-1',   # Link 1
#     'https://www.kanshudo.com/collections/iknow/IK-101',  # Link 2
#     'https://www.kanshudo.com/collections/iknow/IK-201',  # Link 3
#     'https://www.kanshudo.com/collections/iknow/IK-301',  # Link 4
#     'https://www.kanshudo.com/collections/iknow/IK-401',  # Link 5
#     'https://www.kanshudo.com/collections/iknow/IK-501',  # Link 6
#     'https://www.kanshudo.com/collections/iknow/IK-601',  # Link 7
#     'https://www.kanshudo.com/collections/iknow/IK-701',  # Link 8
#     'https://www.kanshudo.com/collections/iknow/IK-802',  # Link 9
#     'https://www.kanshudo.com/collections/iknow/IK-901',  # Link 10
#     'https://www.kanshudo.com/collections/iknow/IK-1001', # Link 11
#     'https://www.kanshudo.com/collections/iknow/IK-1102', # Link 12
#     'https://www.kanshudo.com/collections/iknow/IK-1201', # Link 13
#     'https://www.kanshudo.com/collections/iknow/IK-1301', # Link 14
#     'https://www.kanshudo.com/collections/iknow/IK-1401', # Link 15
#     'https://www.kanshudo.com/collections/iknow/IK-1501', # Link 16
#     'https://www.kanshudo.com/collections/iknow/IK-1601', # Link 17
#     'https://www.kanshudo.com/collections/iknow/IK-1701', # Link 18
#     'https://www.kanshudo.com/collections/iknow/IK-1801', # Link 19
#     'https://www.kanshudo.com/collections/iknow/IK-1901', # Link 20
#     'https://www.kanshudo.com/collections/iknow/IK-2001', # Link 21
#     'https://www.kanshudo.com/collections/iknow/IK-2101', # Link 22
#     'https://www.kanshudo.com/collections/iknow/IK-2201', # Link 23
#     'https://www.kanshudo.com/collections/iknow/IK-2301', # Link 24
#     'https://www.kanshudo.com/collections/iknow/IK-2401', # Link 25
#     'https://www.kanshudo.com/collections/iknow/IK-2502', # Link 26
#     'https://www.kanshudo.com/collections/iknow/IK-2601', # Link 27
#     'https://www.kanshudo.com/collections/iknow/IK-2701', # Link 28
#     'https://www.kanshudo.com/collections/iknow/IK-2801', # Link 29
#     'https://www.kanshudo.com/collections/iknow/IK-2901', # Link 30
#     'https://www.kanshudo.com/collections/iknow/IK-3001', # Link 31
#     'https://www.kanshudo.com/collections/iknow/IK-3101', # Link 32
#     'https://www.kanshudo.com/collections/iknow/IK-3201', # Link 33
#     'https://www.kanshudo.com/collections/iknow/IK-3301', # Link 34
#     'https://www.kanshudo.com/collections/iknow/IK-3401', # Link 35
#     'https://www.kanshudo.com/collections/iknow/IK-3501', # Link 36
#     'https://www.kanshudo.com/collections/iknow/IK-3601', # Link 37
#     'https://www.kanshudo.com/collections/iknow/IK-3701', # Link 38
#     'https://www.kanshudo.com/collections/iknow/IK-3801', # Link 39
#     'https://www.kanshudo.com/collections/iknow/IK-3901', # Link 40
#     'https://www.kanshudo.com/collections/iknow/IK-4001', # Link 41
#     'https://www.kanshudo.com/collections/iknow/IK-4101', # Link 42
#     'https://www.kanshudo.com/collections/iknow/IK-4201', # Link 43
#     'https://www.kanshudo.com/collections/iknow/IK-4301', # Link 44
#     'https://www.kanshudo.com/collections/iknow/IK-4401', # Link 45
#     'https://www.kanshudo.com/collections/iknow/IK-4501', # Link 46
#     'https://www.kanshudo.com/collections/iknow/IK-4601', # Link 47
#     'https://www.kanshudo.com/collections/iknow/IK-4701', # Link 48
#     'https://www.kanshudo.com/collections/iknow/IK-4801', # Link 49
#     'https://www.kanshudo.com/collections/iknow/IK-4901', # Link 50
#     'https://www.kanshudo.com/collections/iknow/IK-5001', # Link 51
#     'https://www.kanshudo.com/collections/iknow/IK-5101', # Link 52
#     'https://www.kanshudo.com/collections/iknow/IK-5201', # Link 53
#     'https://www.kanshudo.com/collections/iknow/IK-5301', # Link 54
#     'https://www.kanshudo.com/collections/iknow/IK-5401', # Link 55
#     'https://www.kanshudo.com/collections/iknow/IK-5501', # Link 56
#     'https://www.kanshudo.com/collections/iknow/IK-5601', # Link 57
#     'https://www.kanshudo.com/collections/iknow/IK-5701', # Link 58
#     'https://www.kanshudo.com/collections/iknow/IK-5801', # Link 59
#     'https://www.kanshudo.com/collections/iknow/IK-5903', # Link 60
# ]


# Kata yang ingin dicari
word_to_find = '勤'

# Loop untuk memeriksa setiap link
for index, url in enumerate(urls):
    print(f'CEK {url}...')
    if check_word_in_page(url, word_to_find):
        print(f'Kata "{word_to_find}" ditemukan di {url}!')
        break
    else:
        print(f'Kata "{word_to_find}" tidak ditemukan di {url}.')

