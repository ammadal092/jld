function toggleVisibility(buttonId, tdId) {
    document.getElementById(buttonId).addEventListener('click', function() {
        var spanElement = document.querySelector(`#${tdId} span`);
        spanElement.classList.toggle('d-none');
        spanElement.classList.toggle('d-block');
    });
}

// Panggil fungsi untuk setiap tombol
for (let i = 1; i <= 100; i++) {
    toggleVisibility('button' + i, 'd' + i);
}

