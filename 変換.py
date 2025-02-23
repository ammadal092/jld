import pyperclip
kata1='日本が日本でなくなる？観光公害どう対策？インバウンド目標は無理'
nomor="44"
kata2="こうがいpolusi/negatif たいさくtindakanuntukmasalah もくひょうsasaran/tujuan むりmustahil inbound>mengarahkewistawanasing"
input1 = '<td>'+kata1+'<button id="button'+nomor+'" type="button" class="btn btn-secondary btn-sm">確認</button></td><td id="d'+nomor+'"><span class="d-none">'+kata2+'</span></td>'


print(input1)
pyperclip.copy(input1)