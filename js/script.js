// ===== Personal Learning Platform - JavaScript Interactions =====

document.addEventListener("DOMContentLoaded", function () {

    // ======================================================
    // 1. NAVIGATION - Active state management
    // ======================================================

    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(function (link) {

        link.addEventListener("click", function () {

            navLinks.forEach(function (navLink) {
                navLink.classList.remove("active");
            });

            link.classList.add("active");
        });

    });


    // ======================================================
    // 2. MESSAGE CONTAINER
    // ======================================================

    const messageContainer =
        document.getElementById("interaction-message");


    function updateMessage(message) {

        if (messageContainer) {
            messageContainer.textContent = message;
        }

    }


    // ======================================================
    // 3. CONTINUE LEARNING BUTTONS
    // ======================================================

    const continueButtons =
        document.querySelectorAll(".continue-btn");

    continueButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const courseCard =
                button.closest(".course-card");

            if (courseCard) {

                const courseTitle =
                    courseCard.querySelector("h3");

                if (courseTitle) {

                    updateMessage(
                        "Continuing your learning journey with " +
                        courseTitle.textContent +
                        "."
                    );

                } else {

                    updateMessage(
                        "Continuing your learning journey."
                    );

                }

            }

        });

    });


    // ======================================================
    // 4. RECOMMENDATION BUTTONS
    // ======================================================

    const recommendationButtons =
        document.querySelectorAll(".start-rec-btn");

    recommendationButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const recommendationCard =
                button.closest(".rec-card");

            if (recommendationCard) {

                const topic =
                    recommendationCard.querySelector("h3");

                if (topic) {

                    updateMessage(
                        topic.textContent +
                        " has been added to your learning plan."
                    );

                } else {

                    updateMessage(
                        "Recommendation added to your learning plan."
                    );

                }

            }

        });

    });


    // ======================================================
    // 5. PRACTICE BUTTONS
    // ======================================================

    const practiceButtons =
        document.querySelectorAll(".practice-btn");

    practiceButtons.forEach(function (button) {

        button.addEventListener("click", function () {

            const practiceCard =
                button.closest(".practice-card");

            if (practiceCard) {

                const practiceTitle =
                    practiceCard.querySelector("h3");

                if (practiceTitle) {

                    updateMessage(
                        "Starting " +
                        practiceTitle.textContent +
                        " practice."
                    );

                } else {

                    updateMessage(
                        "Starting practice session."
                    );

                }

            }

        });

    });


    // ======================================================
    // 6. CONSOLE MESSAGE FOR DEBUGGING
    // ======================================================

    console.log(
        "Personal Learning Platform · JavaScript loaded successfully."
    );

});