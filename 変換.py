import pyperclip
kata1='彼に手紙を渡した'
nomor="24"
kata2="わたります"
input1 = '<td>'+kata1+'<button id="button'+nomor+'" type="button" class="btn btn-secondary btn-sm">確認</button></td><td id="d'+nomor+'"><span class="d-none">'+kata2+'</span></td>'


print(input1)
pyperclip.copy(input1)