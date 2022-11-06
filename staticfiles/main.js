console.log("Sanity check!");

// FREE OFFERING
fetch("/config/")
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);

    let submitBtnFree = document.querySelector("#submitBtnFree");
    if (submitBtnFree !== null) {
      submitBtnFree.addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/create-checkout-session-free/")
          .then((result) => {
            return result.json();
          })
          .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({ sessionId: data.sessionId });
          })
          .then((res) => {
            console.log(res);
          });
      });
    }
  });

// BASIC OFFERING
fetch("/config/")
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);

    let submitBtn = document.querySelector("#submitBtn");
    if (submitBtn !== null) {
      submitBtn.addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/create-checkout-session/")
          .then((result) => {
            return result.json();
          })
          .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({ sessionId: data.sessionId });
          })
          .then((res) => {
            console.log(res);
          });
      });
    }
  });

// PREMIUM OFFERING

fetch("/config/")
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);

    let submitBtnBasic = document.querySelector("#submitBtnBasic");
    if (submitBtnBasic !== null) {
      submitBtnBasic.addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/create-checkout-session-basic/")
          .then((result) => {
            return result.json();
          })
          .then((data) => {
            console.log(data);
            // Redirect to Stripe Checkout
            return stripe.redirectToCheckout({ sessionId: data.sessionId });
          })
          .then((res) => {
            console.log(res);
          });
      });
    }
  });

// const manageBtn = document.getElementById("manage-survey");
// const manageDropDown = document.getElementById("manage-dropdown");

// manageBtn.addEventListener("click", function () {
//   manageDropDown.classList.remove("hidden");
// });

// MOBILE MENU

const closeMenu = document.getElementById("close-menu");
const mobileMenu = document.getElementById("mobile-menu");

closeMenu.addEventListener("click", function () {
  mobileMenu.classList.add("hidden");
});

const openMenu = document.getElementById("open-menu");

openMenu.addEventListener("click", function () {
  mobileMenu.classList.remove("hidden");
});
