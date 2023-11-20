function googleSearch() {
    console.log('hello');
  // Get the search query from the input field
  var query = document.getElementById("search-bar").value;

  // Redirect to Google search results page with the query
  window.location.href =
    "https://www.google.com/search?q=" + encodeURIComponent(query);
}

function imageSearch() {
  // Get the search query from the input field
  var query = document.getElementById("search-bar").value;

  // Redirect to Google image search results page with the query
  window.location.href =
    "https://www.google.com/search?tbm=isch&q=" + encodeURIComponent(query);
}

function advancedSearch() {
  // Get values from the advanced search fields
  var allWords = document.getElementById("all-words").value;
  var exactPhrase = document.getElementById("exact-phrase").value;
  var anyWords = document.getElementById("any-words").value;
  var noneWords = document.getElementById("none-words").value;

  // Construct the advanced search query (customize as needed)
  var query =
    "allinurl:" +
    encodeURIComponent(allWords) +
    " " +
    encodeURIComponent(exactPhrase) +
    " " +
    encodeURIComponent(anyWords) +
    " -" +
    encodeURIComponent(noneWords);

  // Redirect to Google search results page with the advanced search query
  window.location.href =
    "https://www.google.com/search?q=" + encodeURIComponent(query);
}

function feelingLucky() {
  // Get the search query from the input field
  var query = document.getElementById("search-bar").value;

  // Redirect to the first Google search result page with the query
  window.location.href =
    "https://www.google.com/search?q=" + encodeURIComponent(query) + "&btnI";
}
