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

// ANIMATION

// $(window).on("load", function () {
//   $(".load-wrapper").fadeOut("slow");
// });

barba.init({
  transitions: [
    {
      name: "opacity-transition",
      leave(data) {
        return gsap.to(data.current.container, {
          opacity: 0,
        });
      },
      enter(data) {
        return gsap.from(data.next.container, {
          opacity: 0,
        });
      },
    },
  ],
});

const manageBtn = document.getElementById("manage-survey");
const manageDropDown = document.getElementById("manage-dropdown");

manageBtn.addEventListener("click", function () {
  manageDropDown.classList.remove("hidden");
});
