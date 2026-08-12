const cards = document.querySelector('.overview-cards');
const arrowRight = document.querySelector('.overview-arrow-right');
const arrowLeft = document.querySelector('.overview-arrow-left');
const allCards = document.querySelectorAll('.overview-card');

let scrollPx = parseInt(getComputedStyle(allCards[0]).maxWidth) + 30;
console.log('scrollpx: ', scrollPx);

arrowRight.addEventListener('click', () => {
  cards.scrollBy({ left: scrollPx, behavior: 'smooth' });
  arrowLeft.style.display = 'flex';
});

arrowLeft.addEventListener('click', () => {
  cards.scrollBy({ left: -scrollPx, behavior: 'smooth' });
  arrowRight.style.display = 'flex';
});


if (window.innerWidth < 450) {
  console.log('width ted: ',window.screen.width);
  console.log("prcam to");
  console.log('scrollpx: ', scrollPx);
  allCards.forEach((card => {
    const newWidth = (window.screen.width - 700) + 'px';
    card.style.maxWidth = newWidth;
    card.style.minWidth = newWidth;
    console.log('ejj', getComputedStyle(card).maxWidth);
  }));
  scrollPx = parseInt(getComputedStyle(allCards[0]).maxWidth) + 35;
  arrowRight.style.display = 'flex';
}

if (window.innerWidth < 990) {
  console.log('width ted: ',window.innerWidth);
  console.log("prcam to");
  console.log('scrollpx: ', scrollPx);
  allCards.forEach((card => {
    const newWidth = (window.innerWidth - 45) + 'px';
    card.style.maxWidth = newWidth;
    card.style.minWidth = newWidth;
    console.log('ejj', getComputedStyle(card).maxWidth);
  }));
  scrollPx = parseInt(getComputedStyle(allCards[0]).maxWidth) + 35;
  arrowRight.style.display = 'flex';
}

function isAtEnd() {
  // Přidáváme malou toleranci (1px) kvůli zaokrouhlování pixelů na některých displejích

  //cards.scrollLeft - kolik px overview-cards zmizelo za okrajem
  //cards.clientWidth - šířka oblasti viditelných karet
  //cards.scrollwidth = celková šířka overview-cards
  const isAtEnd = cards.scrollLeft + cards.clientWidth >= cards.scrollWidth - 1;

  if (isAtEnd) {
    console.log('Už není kam scrollnout doprava!');
    // Zde můžeš šipku schovat nebo jí dát třídu pro zšednutí:
    arrowRight.style.display = 'none';
    arrowLeft.style.display = 'flex';
  } else {
    arrowRight.style.display = 'flex'; // nebo 'block'
  }
}

function isAtBeginning() {
  const isAtBeginning = cards.scrollLeft == 0;

  if (isAtBeginning) {
    console.log('Neni kam scrollnout doleva');
    arrowLeft.style.display = 'none';
    arrowRight.style.display = 'flex';
  } else {
    arrowLeft.style.display = 'flex';
  }
}

// 2. Kontrola při každém posunu (scrollu)
cards.addEventListener('scroll', () => {

  isAtEnd();
  isAtBeginning();


});

window.addEventListener('resize', () => {
  console.log('New width:', window.innerWidth);
  if (window.innerWidth < 625) {
    console.log("negr");

    console.log('scrollpx: ', scrollPx);
    allCards.forEach((card => {
      const newWidth = (window.innerWidth - 50) + 'px';
      card.style.maxWidth = newWidth;
      card.style.minWidth = newWidth;
      console.log('ejj', getComputedStyle(card).maxWidth);
    }));
    scrollPx = parseInt(getComputedStyle(allCards[0]).maxWidth) + 35;
  }
  else if (window.innerWidth < 748) {

    console.log('scrollpx: ', scrollPx);
    allCards.forEach((card => {
      const newWidth = (window.innerWidth - 90) / 2 + 'px';
      card.style.maxWidth = newWidth;
      card.style.minWidth = newWidth;
      console.log('ejj', getComputedStyle(card).maxWidth);
    }));
    scrollPx = parseInt(getComputedStyle(allCards[0]).maxWidth) + 35;
  }
  else if (window.innerWidth < 875) {
    console.log('scrollpx: ', scrollPx);
    allCards.forEach((card => {
      const newWidth = (window.innerWidth - 90) / 2 + 'px';
      card.style.maxWidth = newWidth;
      card.style.minWidth = newWidth;
      console.log('ejj', getComputedStyle(card).maxWidth);
    }));
    scrollPx = parseInt(getComputedStyle(allCards[0]).maxWidth) + 30;

    isAtEnd();
    isAtBeginning();
  } else {
    arrowRight.style.display = 'none';
    arrowLeft.style.display = 'none';
    allCards.forEach((card => {
      card.style.maxWidth = '';
      card.style.minWidth = '';
      console.log('ejj', getComputedStyle(card).maxWidth);
    }));
  }


});


const dateFrom = document.getElementById("date-form");
const dateTo = document.getElementById("date-to");

flatpickr("#kalendar", {
  showMonths: 2, // <--- Zapne 2 kalendáře vedle sebe
  dateFormat: "d.m.Y",
  mode: "range",   // Umožní vybrat rozsah (od - do)
  locale: "cs",

  onReady: function (selectedDates, dateStr, instance) {
    const footer = document.createElement("div");
    footer.classList.add('calendar-footer');

    const btnClear = document.createElement('a');
    btnClear.textContent = 'Smazat';
    btnClear.classList.add('calendar-clear-btn');
    btnClear.addEventListener("click", () => {
        instance.clear();
        instance.close();
      });

    const btnSearch = document.createElement('a');
    btnSearch.textContent = 'Hledat';
    btnSearch.classList.add('calendar-search-btn');

    footer.appendChild(btnClear);
    footer.appendChild(btnSearch);

    instance.calendarContainer.appendChild(footer);
  },

  onChange: function (selectedDates, dateStr, instance) {
    if (selectedDates[0]) {
      dateFrom.value = instance.formatDate(selectedDates[0], "d.m.Y");
    } else {
      dateFrom.value = "";
    }

    if (selectedDates[1]) {
      dateTo.value = instance.formatDate(selectedDates[1], "d.m.Y");
    } else {
      dateTo.value = "";
    }
  }
});


const searchButton = document.getElementById('search-button');
const dateDropdown = document.getElementById("dateDropdown");


const helpButton = document.getElementById('help-button');
const helpDialog = document.getElementById('help-dialog');

helpButton.addEventListener("click", (event) => {
  event.stopPropagation();
  helpDialog.classList.toggle('open');
});



const dateButton = document.getElementById("kalendar");
const toolbarSearch = document.getElementById("toolbar-search");
const dateInputPicker = document.getElementById("date-input-picker");
dateButton.addEventListener("click", (event) => {
  event.stopPropagation();
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  productsDropdown.classList.remove('open');
  adjustDropdown.classList.remove("open");
  extensionsDropdown.classList.remove("open");
  amountDropdown.classList.remove("open");
  toolbarSearch.classList.toggle("search-date-active");
  dateButton.classList.toggle("dateBtn-date-active");
  dateInputPicker.classList.toggle("date-input-picker-active");
  searchButton.classList.toggle('input-is-active');
  searchButton.classList.toggle('search-button');

});



const productsDropdown = document.getElementById('productsDropdown');
const productsButton = document.getElementById('dropdownBtn');
// 1. Přepínání menu po kliknutí na tlačítko
productsButton.addEventListener('click', (event) => {
  // Zamezí tomu, aby se kliknutí ihned propagovalo na document
  event.stopPropagation();
  productsDropdown.classList.toggle('open');
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  adjustDropdown.classList.remove("open");
  extensionsDropdown.classList.remove("open");
  amountDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
  toolbarSearch.classList.remove("search-date-active");
  searchButton.classList.remove('input-is-active');
  searchButton.classList.add('search-button');
});



const productCardBtn1 = document.getElementById('product-card-footer-btn1');
const productCardDropdown1 = document.getElementById('product-card-footer-dropdown-menu1');

productCardBtn1.addEventListener("click", (event) => {
  event.stopPropagation();
  productCardDropdown1.classList.toggle('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  adjustDropdown.classList.remove("open");
  amountDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  extensionsDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  toolbarSearch.classList.remove("search-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
});

const productCardBtn2 = document.getElementById('product-card-footer-btn2');
const productCardDropdown2 = document.getElementById('product-card-footer-dropdown-menu2');

productCardBtn2.addEventListener("click", (event) => {
  event.stopPropagation();
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.toggle('open');
  productCardDropdown3.classList.remove('open');
  adjustDropdown.classList.remove("open");
  amountDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  extensionsDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  toolbarSearch.classList.remove("search-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
});

const productCardBtn3 = document.getElementById('product-card-footer-btn3');
const productCardDropdown3 = document.getElementById('product-card-footer-dropdown-menu3');

productCardBtn3.addEventListener("click", (event) => {
  event.stopPropagation();
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.toggle('open');
  adjustDropdown.classList.remove("open");
  amountDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  extensionsDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  toolbarSearch.classList.remove("search-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
});


const adjustDropdownButton = document.getElementById("adjust-button");
const adjustDropdownButtonPhone = document.getElementById("adjust-button-phone");
const adjustDropdown = document.getElementById("adjustDropdown");

adjustDropdownButton.addEventListener("click", (event) => {
  event.stopPropagation();
  adjustDropdown.classList.toggle("open");
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  amountDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  extensionsDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  toolbarSearch.classList.remove("search-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
});

adjustDropdownButtonPhone.addEventListener("click", (event) => {
  event.stopPropagation();
  adjustDropdown.classList.toggle("open");
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  amountDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  extensionsDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  toolbarSearch.classList.remove("search-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
});




const amountDropdownButton = document.getElementById("amountButton");
const amountDropdown = document.getElementById("amountDropdown");

amountDropdownButton.addEventListener("click", (event) => {
  event.stopPropagation();
  amountDropdown.classList.toggle("open");
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  adjustDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  extensionsDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
  toolbarSearch.classList.remove("search-date-active");
  searchButton.classList.toggle('input-is-active');
  searchButton.classList.toggle('search-button');
});





// Kliknutí na položku s podpoložkou
const dropdownProductsBtn = document.getElementById('dropdownProductsBtn');
const navDropdown = document.getElementById('dropdownProductsMenu');

dropdownProductsBtn.addEventListener('click', () => {
  // Přidá/odebere třídu .open, což spustí animaci max-height
  navDropdown.classList.toggle('open');
  dropdownProductsBtn.classList.toggle("pressed");
});



// Kliknutí na položku s podpoložkou
const dropdownExtensionsBtn = document.getElementById('dropdownExtensionsBtn');
const dropdownExtensionsMenu = document.getElementById('dropdownExtensionsMenu');

dropdownExtensionsBtn.addEventListener('click', () => {
  // Přidá/odebere třídu .open, což spustí animaci max-height
  dropdownExtensionsMenu.classList.toggle('open');
  dropdownExtensionsBtn.classList.toggle("pressed");
});




// Kliknutí na položku s podpoložkou
const dropdownHelpBtn = document.getElementById('dropdownHelpBtn');
const dropdownHelpMenu = document.getElementById('dropdownHelpMenu');

dropdownHelpBtn.addEventListener('click', () => {
  // Přidá/odebere třídu .open, což spustí animaci max-height
  dropdownHelpMenu.classList.toggle('open');
  dropdownHelpBtn.classList.toggle("pressed");
});








const extensionsDropdown = document.getElementById("extensionsDropdown");
const extensionsButton = document.getElementById("extensionsDropdownBtn");

extensionsButton.addEventListener('click', (event) => {
  event.stopPropagation();
  extensionsDropdown.classList.toggle('open');
  productCardDropdown1.classList.remove('open');
  productCardDropdown2.classList.remove('open');
  productCardDropdown3.classList.remove('open');
  adjustDropdown.classList.remove("open");
  productsDropdown.classList.remove('open');
  amountDropdown.classList.remove("open");
  dateButton.classList.remove("dateBtn-date-active");
  dateInputPicker.classList.remove("date-input-picker-active");
  toolbarSearch.classList.remove("search-date-active");
  searchButton.classList.remove('input-is-active');
  searchButton.classList.add('search-button');
});


// 2. Zavření menu, pokud kliknete kamkoliv jinam na stránce
document.addEventListener('click', (event) => {
  if (!productsDropdown.contains(event.target)
    && !extensionsDropdown.contains(event.target)
    && !amountDropdown.contains(event.target)
    && !adjustDropdown.contains(event.target)
    && !dateDropdown.contains(event.target)
    && !productCardDropdown1.contains(event.target)
    && !productCardDropdown2.contains(event.target)
    && !productCardDropdown3.contains(event.target)) {

    productCardDropdown1.classList.remove('open');
    productCardDropdown2.classList.remove('open');
    productCardDropdown3.classList.remove('open');
    productsDropdown.classList.remove('open');
    adjustDropdown.classList.remove("open");
    extensionsDropdown.classList.remove("open");
    amountDropdown.classList.remove("open");
    dateButton.classList.remove("dateBtn-date-active");
    dateInputPicker.classList.remove("date-input-picker-active");
    toolbarSearch.classList.remove("search-date-active");
    searchButton.classList.remove('input-is-active');
    searchButton.classList.add('search-button');
  }
});







const hamburgerBtn = document.getElementById('hamburgerBtn');
const navLinks = document.getElementById('navbar-menu');

hamburgerBtn.addEventListener('click', () => {
  // Přidá/odebere třídu .active na kontejner odkazů
  navLinks.classList.toggle('active');
});