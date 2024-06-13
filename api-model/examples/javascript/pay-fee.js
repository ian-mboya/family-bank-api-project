const raw = "{\r\n  \"student_id\": 4265267,\r\n  \"school_id\": 1,\r\n  \"student_name\": \"Malcom Boy\",\r\n  \"payment_method\": \"Credit Card\",\r\n  \"payment_reason\": \"Tuition Fee\",\r\n  \"amount\": 15000,\r\n  \"payment_date\": \"2024-06-11T16:07:33.699Z\"\r\n}";

const requestOptions = {
  method: "POST",
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/fee/\n", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));