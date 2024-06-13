var options = new RestClientOptions("http://127.0.0.1:8000")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("/fee/
", Method.Post);
var body = @"{
" + "\n" +
@"  ""student_id"": 4265267,
" + "\n" +
@"  ""school_id"": 1,
" + "\n" +
@"  ""student_name"": ""Malcom Boy"",
" + "\n" +
@"  ""payment_method"": ""Credit Card"",
" + "\n" +
@"  ""payment_reason"": ""Tuition Fee"",
" + "\n" +
@"  ""amount"": 15000,
" + "\n" +
@"  ""payment_date"": ""2024-06-11T16:07:33.699Z""
" + "\n" +
@"}";
request.AddParameter("text/plain", body,  ParameterType.RequestBody);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);