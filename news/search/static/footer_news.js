// Get the footer element
const footer = document.querySelector('footer');

// Define variable for previous scroll position as existing vertical distance scrolled from the top window
var prevScrollpos = window.pageYOffset;

// Activate the below script when user scrolls up or down
window.addEventListener('scroll', () => {
  
// Define variable for updated scrolling position
var currentScrollPos = window.pageYOffset;
  
// If user is scrolling up
if (prevScrollpos > currentScrollPos) {
    
    // Add the 'invisible' class to the footer
    footer.classList.remove('visible');
    footer.classList.add('invisible');
  }  
  
// If user is scrolling down
else {
    
    // Add the 'visible' class from the footer
    footer.classList.remove('invisible');
    footer.classList.add('visible');
  }

// Update previous scroll position to current scroll position for the next cycle
prevScrollpos = currentScrollPos;
