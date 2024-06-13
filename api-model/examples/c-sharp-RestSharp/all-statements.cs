var options = new RestClientOptions("http://127.0.0.1:8000")
{
  MaxTimeout = -1,
};
var client = new RestClient(options);
var request = new RestRequest("/statements/", Method.Get);
request.AddHeader("", "");
var body = @"";
request.AddParameter("text/plain", body,  ParameterType.RequestBody);
RestResponse response = await client.ExecuteAsync(request);
Console.WriteLine(response.Content);