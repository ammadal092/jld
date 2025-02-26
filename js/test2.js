// Fungsi untuk menambahkan event listener ke setiap tombol
function toggleVisibility(buttonId) {
    document.getElementById(buttonId).addEventListener('click', function() {
        console.log(buttonId + ' ditekan');  // Menampilkan ID tombol yang ditekan

        // Temukan baris (tr) yang mengandung tombol yang ditekan
        var row = document.querySelector(`#${buttonId}`).closest('tr');
        
        // Temukan semua elemen dalam baris yang memiliki kelas 'd-none' atau 'd-block'
        var columns = row.querySelectorAll('.d-none, .d-block');
        
        // Loop untuk mengubah kelas d-none menjadi d-block atau d-block menjadi d-none
        columns.forEach(function(col) {
            if (col.classList.contains("d-none")) {
                col.classList.remove("d-none");
                col.classList.add("d-block");
                //console.log("Status diubah menjadi d-block untuk elemen: ", col);
            } 
            else if (col.classList.contains("d-block")) {
                col.classList.remove("d-block");
                col.classList.add("d-none");
                //console.log("Status diubah menjadi d-none untuk elemen: ", col);
            }
        });
    });
}

// Loop untuk menambahkan event listener pada tombol button1 hingga button1000
for (let i = 1; i <= 1000; i++) {
    let buttonId = 'button' + i;
    if (document.getElementById(buttonId)) {
        toggleVisibility(buttonId); // Jika tombol ada, tambahkan event listener
    }
}
