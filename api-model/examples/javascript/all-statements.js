const myHeaders = new Headers();
myHeaders.append("", "");

const raw = "";

const requestOptions = {
  method: "GET",
  headers: myHeaders,
  body: raw,
  redirect: "follow"
};

fetch("http://127.0.0.1:8000/statements/", requestOptions)
  .then((response) => response.text())
  .then((result) => console.log(result))
  .catch((error) => console.error(error));