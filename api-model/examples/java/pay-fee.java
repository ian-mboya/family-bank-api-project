// OkHttpClient client = new OkHttpClient().newBuilder()
//   .build();
// MediaType mediaType = MediaType.parse("text/plain");
// RequestBody body = RequestBody.create(mediaType, "{\r\n  \"student_id\": 4265267,\r\n  \"school_id\": 1,\r\n  \"student_name\": \"Malcom Boy\",\r\n  \"payment_method\": \"Credit Card\",\r\n  \"payment_reason\": \"Tuition Fee\",\r\n  \"amount\": 15000,\r\n  \"payment_date\": \"2024-06-11T16:07:33.699Z\"\r\n}");
// Request request = new Request.Builder()
//   .url("http://127.0.0.1:8000/fee/
// ")
//   .method("POST", body)
//   .build();
// Response response = client.newCall(request).execute();