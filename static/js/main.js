/**
 * Efeitos Visuais para o Sistema Bottle
 * 
 * Inclui:
 * - Animação de carregamento suave
 * - Efeito de hover em botões/tabelas
 * - Feedback visual para formulários
 * - Botão de scroll para topo
 */

document.addEventListener('DOMContentLoaded', function() {
    console.log('Página carregada no navegador!')
    
    // 1. Efeito de fade-in ao carregar a página
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease-in-out';
        document.body.style.opacity = '1';
    }, 100);

});
document.addEventListener('DOMContentLoaded', () => {
    // 1. Seleciona todos os contêineres de carrossel na página
    const carrossels = document.querySelectorAll('.image-carrossel');

    // Itera sobre cada um dos carrosséis encontrados
    carrossels.forEach(carrossel => {
        
        // 2. Define os elementos específicos deste carrossel
        const slidesContainer = carrossel.querySelector('.slides-container');
        const slides = carrossel.querySelectorAll('.slide');
        const prevBtn = carrossel.querySelector('.prev-btn');
        const nextBtn = carrossel.querySelector('.next-btn');

        // Se não houver slides (imagens), não faz nada
        if (slides.length === 0) return;
        
        let currentIndex = 0; // Índice de controle para este carrossel

        // 3. Função para mover os slides
        function updateCarrossel() {
            // Calcula o deslocamento horizontal (em porcentagem)
            // Se currentIndex=1, desloca em -100% (para mostrar a segunda imagem)
            const offset = -currentIndex * 100;
            slidesContainer.style.transform = `translateX(${offset}%)`;
        }

        // 4. Adiciona o evento de clique ao botão PRÓXIMO
        nextBtn.addEventListener('click', () => {
            if (currentIndex < slides.length - 1) {
                currentIndex++; // Vai para o próximo slide
            } else {
                currentIndex = 0; // Volta ao primeiro (loop)
            }
            updateCarrossel();
        });

        // 5. Adiciona o evento de clique ao botão ANTERIOR
        prevBtn.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--; // Vai para o slide anterior
            } else {
                currentIndex = slides.length - 1; // Vai para o último (loop)
            }
            updateCarrossel();
        });

        // Inicializa a posição do carrossel
        updateCarrossel(); 
    });
});