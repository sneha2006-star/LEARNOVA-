<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Learnova - AI Learning Assistant</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: white;
            width: 500px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.2);
            text-align: center;
        }

        h1 {
            margin-bottom: 15px;
        }

        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;
            resize: none;
        }

        button {
            margin-top: 15px;
            padding: 10px 20px;
            border: none;
            background-color: #4facfe;
            color: white;
            font-size: 16px;
            border-radius: 8px;
            cursor: pointer;
        }

        button:hover {
            background-color: #007bff;
        }

        .answer-box {
            margin-top: 20px;
            text-align: left;
            background: #f4f4f4;
            padding: 15px;
            border-radius: 8px;
            min-height: 60px;
        }

        .loading {
            color: gray;
            font-style: italic;
        }
    </style>
</head>

<body>

<div class="container">
    <h1>🌟 Learnova</h1>
    <p>Your AI Learning Assistant</p>

    <textarea id="question" placeholder="Ask your question here..."></textarea>
    <br>
    <button onclick="askQuestion()">Ask Learnova</button>

    <div class="answer-box" id="answer">
        Your answer will appear here...
    </div>
</div>

<script>
    async function askQuestion() {
        const question = document.getElementById("question").value;
        const answerBox = document.getElementById("answer");

        if (!question) {
            alert("Please enter a question!");
            return;
        }

        answerBox.innerHTML = "<span class='loading'>Thinking...</span>";

        try {
            const response = await fetch("http://localhost:5000/api/ask", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ question: question }),
            });

            const data = await response.json();
            answerBox.innerHTML = data.answer;

        } catch (error) {
            answerBox.innerHTML = "Error connecting to server.";
        }
    }
</script>

</body>
</html>
