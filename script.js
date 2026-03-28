// Welcome button
document.getElementById("start-btn").addEventListener("click", () => {
    alert("Welcome to Learnova! Start Learning Smart 📚");
});

// Quiz data
const quizQuestions = [
    { question: "What is i² (iota square)?", options: ["1", "-1", "0"], answer: "-1" },
    { question: "What is the derivative of x²?", options: ["x", "2x", "x²"], answer: "2x" },
    { question: "What is H₂O commonly known as?", options: ["Water", "Oxygen", "Hydrogen"], answer: "Water" }
];

let currentQuiz = 0;

function loadQuiz() {
    const q = quizQuestions[currentQuiz];
    document.getElementById("quiz-question").textContent = q.question;

    const optionsDiv = document.getElementById("quiz-options");
    optionsDiv.innerHTML = "";

    q.options.forEach(option => {
        const btn = document.createElement("button");
        btn.textContent = option;
        btn.onclick = () => checkAnswer(option);
        optionsDiv.appendChild(btn);
    });

    document.getElementById("result").textContent = "";
}

function checkAnswer(ans) {
    const correct = quizQuestions[currentQuiz].answer;
    const result = document.getElementById("result");

    if (ans === correct) {
        result.textContent = "Correct! ✅";
        result.style.color = "green";
    } else {
        result.textContent = "Wrong Answer ❌ Try Again!";
        result.style.color = "red";
    }
}

// Feedback
document.getElementById("feedback-btn").addEventListener("click", () => {
    const box = document.getElementById("feedback-box");
    const display = document.getElementById("feedback-display");

    if (box.value.trim()) {
        const p = document.createElement("p");
        p.textContent = box.value;
        display.appendChild(p);
        box.value = "";
        alert("Thank you for your feedback!");
    } else {
        alert("Please write something before submitting.");
    }
});

// Init
loadQuiz();
