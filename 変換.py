import pyperclip
kata1='可動時 引っ張られる 取付後 ねじれ'
nomor="41"
kata2="かどうじsaatbisadigerakkan ひっぱられるmenarikmerenggang引っ張る setelahinstalasi berbelit belit memeutar"
input1 = '<td>'+kata1+'<button id="button'+nomor+'" type="button" class="btn btn-secondary btn-sm">確認</button></td><td id="d'+nomor+'"><span class="d-none">'+kata2+'</span></td>'


print(input1)
pyperclip.copy(input1)