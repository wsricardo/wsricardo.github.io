document.addEventListener('DOMContentLoaded', () => {
    // Galeria interativa (já configurada via onclick no HTML, mas podemos adicionar lógica extra aqui se necessário)
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
        item.addEventListener('click', function(e) {
            if (e.target.classList.contains('gallery-info-btn')) {
                // Toggle a exibição de info no clique
                this.classList.toggle('show-info');
            }
        });
    });

    console.log("WSRicardo Polímata Theme carregado.");
});
