from bs4 import BeautifulSoup

# Membaca file HTML 'kanji2.html'
with open('kanji2.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parsing HTML dengan BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Mencari semua <tr> di dalam <tbody>
tbody = soup.find('tbody')

# Memeriksa setiap <tr> di dalam <tbody>
for tr in tbody.find_all('tr'):
    # Mencari <td> dengan class column-1 dalam setiap baris <tr>
    column_1 = tr.find('td', class_='column-1')
    row_class = tr.get('class')[0]  # Mengambil nama row untuk ID tombol, misalnya "row-12"
    
    # Membuat ID tombol berdasarkan nomor row
    row_number = row_class.split('-')[1]
    button_html = f'<button id="button{row_number}" type="button" class="btn btn-secondary btn-sm">確認</button>'

    # Jika <td class="column-1"> ditemukan
    if column_1:
        # Jika ada teks dalam column-1
        if column_1.get_text(strip=True):
            # Menambahkan tombol ke dalam column-1
            column_1.append(BeautifulSoup(button_html, 'html.parser'))
        else:
            # Jika column-1 kosong, tambahkan tombol ke dalam column-2
            column_2 = tr.find('td', class_='column-2')
            if column_2:
                column_2.append(BeautifulSoup(button_html, 'html.parser'))

# Menyimpan perubahan ke dalam file baru
with open('kanji2_updated.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

print("Proses selesai!")
