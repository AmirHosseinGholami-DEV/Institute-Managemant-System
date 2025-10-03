// Developer: Amir Hossein Gholami
// Front-End Programmer: Amir Hossein Gholami
// Back-End Programmer: Amir Hossein Gholami
// Define a class for the observer object
class Observer {
    // The constructor takes a callback function as an argument
    constructor(callback) {
        // Create a new IntersectionObserver instance with the callback
        this.observer = new IntersectionObserver(callback);
    }

    // Define a method to observe an element
    observe(element) {
        this.observer.observe(element);
    }
}

// Define a function to handle the intersection events
function Animation_On_Scroll(Animation_On_Scroll) {
    // Loop through the entries
    Animation_On_Scroll.forEach((Gps_Scroll) => {
        console.log(Gps_Scroll);
        // Check if the element is intersecting
        if (Gps_Scroll.isIntersecting) {
            // Add the show class to the element
            Gps_Scroll.target.classList.add("show");
        } else {
            // Remove the show class from the element
            Gps_Scroll.target.classList.remove("show");
        }
    });
}

// Create a new Observer instance with the Animation_On_Scroll function

const observer = new Observer(Animation_On_Scroll);

// ====================================================

const Animation_Up_Fade = document.querySelectorAll(".Animation_Up_Fade");
Animation_Up_Fade.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));

// ====================================================

// ====================================================

const Animation_Down_Fade = document.querySelectorAll(".Animation_Down_Fade");
Animation_Down_Fade.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));

// ====================================================

// ====================================================

const Animation_Opacity_Fade = document.querySelectorAll(".Animation_Opacity_Fade");
Animation_Opacity_Fade.forEach((Animation_On_Scroll_By_Css_JavaScript) =>
    observer.observe(Animation_On_Scroll_By_Css_JavaScript));

// ====================================================