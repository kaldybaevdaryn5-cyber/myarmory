document.addEventListener('DOMContentLoaded', () => {

    // --- УНИВЕРСАЛЬНАЯ АНИМАЦИЯ ПОЯВЛЕНИЯ ЭЛЕМЕНТОВ ---
    // Этот код будет работать на ВСЕХ страницах, где есть элементы с нужными классами.
    
    // Функция-обработчик для Intersection Observer
    const observerCallback = (entries, observer) => {
        entries.forEach((entry, index) => {
            if (entry.isIntersecting) {
                // Добавляем задержку на основе порядка элемента для каскадного эффекта
                entry.target.style.transitionDelay = `${index * 0.08}s`;
                entry.target.classList.add('is-visible');
                // Перестаем следить за элементом после того, как он появился
                observer.unobserve(entry.target);
            }
        });
    };

    // Создаем "наблюдателя"
    const observer = new IntersectionObserver(observerCallback, {
        threshold: 0.1 // Анимация сработает, когда 10% элемента видно
    });

    // Находим ВСЕ анимируемые элементы на странице и начинаем за ними следить
const animatedItems = document.querySelectorAll('.animated-item, .timeline-node, .news-card-animated, .weapon-card-new, .fade-in-item');    animatedItems.forEach(item => {
        observer.observe(item);
    });


    // --- АНИМАЦИЯ ПОЛОСОК-ИНДИКАТОРОВ НА ДЕТАЛЬНОЙ СТРАНИЦЕ ---
    const statBars = document.querySelectorAll('.stat-bar');
    if (statBars.length > 0) {
        const barObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const bar = entry.target;
                    const value = parseFloat(bar.dataset.value);
                    const max = parseFloat(bar.dataset.max);
                    const percentage = (value / max) * 100;
                    const fill = bar.querySelector('.bar-fill');
                    
                    fill.style.width = `${Math.min(percentage, 100)}%`; // Ограничиваем 100%
                    observer.unobserve(bar);
                }
            });
        }, { threshold: 0.5 }); // Анимация начнется, когда видно 50% полоски

        statBars.forEach(bar => {
            barObserver.observe(bar);
        });
    }


    // --- ЛОГИКА ДЛЯ ФИЛЬТРОВ И СОРТИРОВКИ В КАТАЛОГЕ ---
    const workshopGrid = document.querySelector('.workshop-grid');
    if (workshopGrid) {
        // ... (этот блок остается без изменений, так как он работает только на странице каталога) ...
        const filtersContainer = document.getElementById('workshop-filters');
        const sortSelect = document.getElementById('sort-by');
        const allCards = Array.from(workshopGrid.querySelectorAll('.weapon-card-new'));

        function renderCards() {
            const activeFilter = filtersContainer ? filtersContainer.querySelector('.active').dataset.filter : 'all';
            const sortValue = sortSelect ? sortSelect.value : 'name-asc';

            let cardsToShow = allCards.filter(card => {
                return activeFilter === 'all' || card.dataset.category === activeFilter;
            });

            cardsToShow.sort((a, b) => {
                const sortField = sortValue.split('-')[0];
                const order = sortValue.split('-')[1];
                const valA = a.dataset[sortField];
                const valB = b.dataset[sortField];
                const numA = parseFloat(valA);
                const numB = parseFloat(valB);
                if (!isNaN(numA) && !isNaN(numB)) {
                    return order === 'asc' ? numA - numB : numB - numA;
                } else {
                    return order === 'asc' ? valA.localeCompare(valB) : valB.localeCompare(valA);
                }
            });
            
            workshopGrid.innerHTML = '';
            cardsToShow.forEach(card => workshopGrid.appendChild(card));
        }
        
        if (filtersContainer) {
            filtersContainer.addEventListener('click', (event) => {
                if (!event.target.classList.contains('filter-btn')) return;
                filtersContainer.querySelector('.active').classList.remove('active');
                event.target.classList.add('active');
                renderCards();
            });
        }
        if (sortSelect) {
            sortSelect.addEventListener('change', renderCards);
        }
        
        if (filtersContainer || workshopGrid.querySelectorAll('.weapon-card-new').length > 0 && !filtersContainer) {
           // renderCards(); // Этот вызов может быть причиной проблемы, давай его пока уберем для простоты
        }
    }
});

// --- ЛОГИКА ДЛЯ ФИЛЬТРАЦИИ ТЕХНИКИ ---

const vehicleFilters = document.getElementById('vehicle-filters');
const vehicleCards = document.querySelectorAll('.vehicle-card');

if (vehicleFilters && vehicleCards.length > 0) {
    vehicleFilters.addEventListener('click', (event) => {
        if (!event.target.classList.contains('filter-btn')) return;

        vehicleFilters.querySelector('.active').classList.remove('active');
        event.target.classList.add('active');

        const filterValue = event.target.dataset.filter;

        vehicleCards.forEach(card => {
            if (filterValue === 'all' || card.dataset.category === filterValue) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    });
}
// --- ЛОГИКА ДЛЯ ВЫПАДАЮЩЕГО МЕНЮ ПРОФИЛЯ ---
const profileMenuButton = document.getElementById('profile-menu-button');
const profileMenu = document.getElementById('profile-menu');

if (profileMenuButton && profileMenu) {
    // Показываем/скрываем меню по клику на кнопку
    profileMenuButton.addEventListener('click', (event) => {
        event.stopPropagation(); // Останавливаем "всплытие" клика
        profileMenu.classList.toggle('is-active');
    });

    // Скрываем меню, если кликнуть куда-угодно за его пределами
    window.addEventListener('click', () => {
        if (profileMenu.classList.contains('is-active')) {
            profileMenu.classList.remove('is-active');
        }
    });
}