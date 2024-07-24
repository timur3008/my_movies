const tabs = document.querySelectorAll('.movie__tab');
const contents = document.querySelectorAll('.movie__tab-content');
let index = 0;

tabs.forEach(tab => tab.addEventListener('click', event => {
    tabs[index].classList.remove('movie__tab_active');
    contents[index].classList.remove('movie__tab-content_active');
    index = Number.parseInt(event.currentTarget.dataset.index);
    tabs[index].classList.add('movie__tab_active');
    contents[index].classList.add('movie__tab-content_active');
}));

const filterItems = document.querySelectorAll('.filter__item');

filterItems.forEach(item => item.addEventListener('click', event => {
    event.currentTarget.lastElementChild.classList.toggle('filter__list_active');
    filterItems.forEach(filterItem => {
        if(filterItem !== event.currentTarget && 
            filterItem.lastElementChild.classList.contains('filter__list_active')) {
            filterItem.lastElementChild.classList.remove('filter__list_active');
        }
    })
}));

const filterLinks = document.querySelectorAll('.filter__link');
const filterButtons = document.querySelectorAll('.filter__button');

let filters = localStorage.getItem('filters') != null ? JSON.parse(localStorage.getItem('filters')) : { 
    'genre': 'all',
    'country': 'all',
    'yearFrom': 0,
    'yearTo': 0
};

filterLinks.forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const parent = event.currentTarget.parentElement;
        switch(parent.dataset.action) {
            case 'genre': filters.genre = event.currentTarget.innerText;
                break;
            case 'country': filters.country = event.currentTarget.innerText;
                break;
            case 'yearFrom': filters.yearFrom = event.currentTarget.innerText;
                break;
            case 'yearTo': filters.yearTo = event.currentTarget.innerText;
                break;
            default: return;
        }
        event.currentTarget.parentElement.previousElementSibling.innerText = event.currentTarget.innerText;
    });
});
filterButtons.forEach(button => {
    button.addEventListener('click', event => {
        event.preventDefault();

        const path = 'http://127.0.0.1:8000/content/'
        const category = location.href.split('/').find(name => (name == 'anime' || name == 'series' || name == 'cartoons' || name == 'films'))

        if(event.currentTarget.innerText === 'Сбросить') {
            localStorage.removeItem('filters');
            location.href = `${path}${category}`
        } else {
            const { genre, country, yearFrom, yearTo } = filters;
            localStorage.setItem('filters', JSON.stringify(filters))
            location.href = `${path}${category}/genre(${genre})/country(${country})/yearFrom(${yearFrom})/yearTo(${yearTo})`
        }
    });
});

